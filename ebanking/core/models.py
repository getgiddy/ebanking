import random
import string
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
    ('F', 'Female')
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


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    country = CountryField()
    state = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pin = models.IntegerField()
    image = models.ImageField(width_field=300, height_field=300, upload_to='profile_pics')
    ip_address = models.GenericIPAddressField()


class Account(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    account_name = models.CharField(max_length=64)
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    account_balance = models.FloatField()
    tac = models.CharField(max_length=4, default=generate_random_digits)
    tax = models.CharField(max_length=4, default=generate_random_digits)


class Beneficiary(models.Model):
    beneficiary_name = models.CharField(max_length=64)
    beneficiary_phone = models.CharField(max_length=15)
    beneficiary_address = models.CharField(max_length=255)
    beneficiary_email = models.EmailField()
    beneficiary_bank = models.CharField(max_length=64)
    beneficiary_account = models.IntegerField()
    swift = models.CharField(max_length=24)
    iban = models.CharField(max_length=24)


class Transaction(models.Model):
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    transaction_ref = models.CharField(max_length=16, default=generate_transaction_ref)
    transaction_amount = models.FloatField()
    transaction_fee = models.FloatField()
    transaction_date = models.DateTimeField(default=timezone.now)