from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic.edit import FormView

from core.forms import ApplicationForm
from core.models import Application


def home(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = ApplicationForm
    success_url = '/register/application_recieved/'

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
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
    return render(request, 'dashboard/index.html')


def transactions(request):
    return render(request, 'dashboard/transactions.html')


def profile(request):
    return render(request, 'dashboard/profile.html')


def deposit(request):
    return render(request, 'dashboard/deposit.html')


def withdraw(request):
    return render(request, 'dashboard/withdraw.html')


def transfer(request):
    return render(request, 'dashboard/transfer.html')
