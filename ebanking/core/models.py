import random
import string
from django.core.validators import validate_integer
from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.utils import timezone


MARITAL_STATUS_CHOICES = (
    ('S', 'Single'),
    ('M', 'Married'),
    ('D', 'Divorced'),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Rather not say'),
)

ACCOUNT_TYPE_CHOICES = (
    ('S', 'Savings'),
    ('C', 'Current'),
    ('F', 'Fixed Deposit'),
)

def generate_random_digits():
    return random.randint(1000, 9999)


def generate_transaction_ref():
    string_length = 16
    letter_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letter_and_digits) for i in range(string_length)))


def generate_account_number():
    string_length = 10
    digits = string.digits
    return ''.join((random.choice(digits) for i in range(string_length)))


class Application(models.Model):
    firstname = models.CharField(max_length=24)
    lastname = models.CharField(max_length=24)
    email = models.EmailField()
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    country = CountryField()
    state = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pin = models.CharField(max_length=4, validators=[validate_integer])
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    account_name = models.CharField(max_length=64)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    phone = models.CharField(max_length=15, validators=[validate_integer])

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    


class Account(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    account_name = models.CharField(max_length=64)
    account_number = models.CharField(max_length=10, default=generate_account_number, validators=[validate_integer])
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    account_balance = models.FloatField(default=0)
    tac = models.CharField(max_length=4, default=generate_random_digits)
    tax = models.CharField(max_length=4, default=generate_random_digits)


class UserProfile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15, validators=[validate_integer])
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    country = CountryField()
    state = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pin = models.CharField(max_length=4, validators=[validate_integer])
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    ip_address = models.GenericIPAddressField()


class Beneficiary(models.Model):
    beneficiary_name = models.CharField(max_length=64)
    beneficiary_phone = models.CharField(max_length=15, validators=[validate_integer])
    beneficiary_address = models.CharField(max_length=255)
    beneficiary_email = models.EmailField()
    beneficiary_bank = models.CharField(max_length=64)
    beneficiary_account = models.CharField(max_length=15, validators=[validate_integer])
    swift = models.CharField(max_length=24)
    iban = models.CharField(max_length=24)


class Transaction(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    transaction_ref = models.CharField(max_length=16, default=generate_transaction_ref)
    transaction_amount = models.FloatField()
    transaction_fee = models.FloatField()
    transaction_date = models.DateTimeField(default=timezone.now)