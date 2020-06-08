from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
        form.save()
        
        # TODO: send mail to admin and applicant
        
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.cleaned_data)
        print(form.errors)
        return super().form_invalid(form)


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
