import datetime
from dateutil.relativedelta import relativedelta

from django import forms
from django.forms import ValidationError

from allauth.account.forms import LoginForm
from core.models import Application


class ApplicationForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-user",
        'placeholder': "Confirm Password",
    }))

    confirm_pin = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-user",
        'placeholder': "Confirm Pin",
    }))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
    
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
    
        return confirm_password

    def clean_confirm_pin(self):
        pin = self.cleaned_data.get('pin')
        confirm_pin = self.cleaned_data.get('confirm_pin')
    
        if pin != confirm_pin:
            raise ValidationError("Pins do not match")
    
        return confirm_pin

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        max_date = datetime.date.today() + relativedelta(years = -120)
        min_date = datetime.date.today() + relativedelta(years = -18)
        
        if date_of_birth > min_date:
            raise ValidationError("Below legal age of consent")
        elif date_of_birth < max_date:
            raise ValidationError("Invalid date")
    
        return date_of_birth

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "First Name",
        })

        self.fields['lastname'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Last Name",
        })

        self.fields['email'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Email",
        })

        self.fields['phone'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Phone",
        })

        self.fields['username'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Username",
        })

        self.fields['password'].widget = forms.PasswordInput()

        self.fields['password'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Password",
        })

        self.fields['pin'].widget = forms.PasswordInput()

        self.fields['pin'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "4-digit Pin",
        })

        self.fields['address'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Address",
        })

        self.fields['state'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "State",
        })

        self.fields['city'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "City",
        })

        self.fields['date_of_birth'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Date of Birth",
        })

        self.fields['account_name'].widget.attrs.update({
            'class': "form-control form-control-user",
            'placeholder': "Account Name",
        })

        self.fields['account_type'].widget.attrs.update({
            'style': 'width:100%;'
        })

        self.fields['gender'].widget.attrs.update({
            'style': 'width:100%;'
        })

        self.fields['marital_status'].widget.attrs.update({
            'style': 'width:100%;'
        })

        self.fields['country'].widget.attrs.update({
            'style': 'width:100%;'
        })

    class Meta:
        model = Application
        fields = [
            'firstname',
            'lastname',
            'email',
            'phone',
            'gender',
            'marital_status',
            'date_of_birth',
            'address',
            'country',
            'state',
            'city',
            'image',
            'account_name',
            'account_type',
            'username',
            'password',
            'pin',
        ]


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = None
        self.fields['password'].label = None
        self.fields['remember'].label = None

        self.fields["login"].widget.attrs.update({
            'class': 'form-control form-control-user',
            # 'id': 'exampleInputEmail',
            'placeholder': "Enter Email Address or Username",
            'aria-describedby': "emailHelp",
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control form-control-user',
            # 'id': 'exampleInputPassword',
            'placeholder': 'Password',
        })

        self.fields['remember'].widget.attrs.update({
            'class': 'custom-control-input',
            'id': 'customCheck',
        })

    
    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)
