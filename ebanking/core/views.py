from datetime import date

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic.edit import FormView

from core.forms import ApplicationForm, DepositForm, WithdrawalForm, TransferForm
import core.account_actions as account_actions
from core.models import (
    Application,
    Transaction,
    Account,
)


def home(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = ApplicationForm
    success_url = '/register/application_recieved/'

    def form_valid(self, form):
        data = form.cleaned_data
        form.save()
        
        applicant_mail = data.get('email')
        first_name = data.get("firstname")
        last_name = data.get("lastname")
        applicant_message = f'Dear {first_name} {last_name},\nYour application has been recieved and is being reviewed.\nYou will be notified as soon as it has been approved.'
        admin_message = f'{first_name} {last_name} just submitted an application.\nReview and approve on the admin panel'
        
        send_mail('Application Recieved', applicant_message, 'localhost', [applicant_mail])
        send_mail('New Application', admin_message, 'localhost', ['admin@site.com'])

        return super(RegisterView, self).form_valid(form)


def application_recieved(request):
    return render(request, 'application_recieved.html')

@login_required
def dashboard(request):
    account = Account.objects.get(user=request.user)
    transactions = Transaction.objects.filter(account=account)
    current_month =  date.today().month
    current_year = date.today().year
    month_transactions = transactions.filter(
            transaction_date__year=current_year, 
            transaction_date__month=current_month
        )

    def total_credits():
        credit = month_transactions.filter(transaction_type='C')
        total = 0
        for transaction in credit:
            total += transaction.transaction_amount
        return total
    
    def total_debits():
        credit = month_transactions.filter(transaction_type='D')
        total = 0
        for transaction in credit:
            total += transaction.transaction_amount
        return total

    context = {
        'transactions': month_transactions[:5],
        'account': account,
        'total_credits': total_credits(),
        'total_debits': total_debits(),
    }

    return render(request, 'dashboard/index.html', context)

@login_required
def transactions(request):
    account = Account.objects.get(user=request.user)
    transactions = Transaction.objects.filter(account=account)

    context = {
        'transactions': transactions,
    }

    return render(request, 'dashboard/transactions.html', context)

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

class DepositFormView(LoginRequiredMixin, FormView):
    form_class = DepositForm
    template_name = 'dashboard/deposit.html'
    success_url = '/dashboard/deposit/'

    def form_valid(self, form):
        account = Account.objects.get(user = self.request.user)
        amount = form.cleaned_data['transaction_amount']

        account_actions.credit(self.request, account, amount)

        return super(DepositFormView, self).form_valid(form)

class WithdrawalFormView(LoginRequiredMixin, FormView):
    form_class = WithdrawalForm
    template_name = 'dashboard/withdraw.html'
    success_url = '/dashboard/withdraw/'

    def form_valid(self, form):
        account = Account.objects.get(user = self.request.user)
        amount = form.cleaned_data['transaction_amount']

        account_actions.withdraw(self.request, account, amount)

        return super(WithdrawalFormView, self).form_valid(form)

class TransferFormView(LoginRequiredMixin, FormView):
    form_class = TransferForm
    template_name = 'dashboard/transfer.html'
    success_url = '/dashboard/transfer/'

    def form_valid(self, form):
        account = Account.objects.get(user = self.request.user)
        amount = form.cleaned_data['transaction_amount']
        beneficiary = form.cleaned_data['beneficiary']

        account_actions.transfer(self.request, account, beneficiary, amount)

        return super(TransferFormView, self).form_valid(form)
