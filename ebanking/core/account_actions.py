from django.contrib import messages
from core.models import Transaction


def withdraw(request, account, amount):
    transaction_rate = 0.01
    transaction_fee = transaction_rate * amount
    transaction = Transaction(
        account = account,
        transaction_type = 'D',
        transaction_amount = amount,
        transaction_fee = transaction_fee,
    )
    total_amount = amount + transaction_fee
    if account.account_balance >= total_amount:
        account.debit(total_amount)
        transaction.save()
        # TODO: Send mail to admin and customer
        return messages.success(request, 'Withdrawal successful')
    else:
        return messages.error(request, 'Insufficient balance')


def transfer(request, account, beneficiary, amount):
    transaction_rate = 0.05
    transaction_fee = transaction_rate * amount
    transaction = Transaction(
        account = account,
        beneficiary = beneficiary,
        transaction_type = 'D',
        transaction_amount = amount,
        transaction_fee = transaction_fee,
    )
    total_amount = amount + transaction_fee
    if account.account_balance >= total_amount:
        account.debit(total_amount)
        transaction.save()
        # TODO: Send mail to admin and customer
        return messages.success(request, 'Transfer successful')
    else:
        return messages.error(request, 'Insufficient balance',)


def credit(request, account, amount):
    transaction = Transaction(
        account = account,
        transaction_type = 'C',
        transaction_amount = amount,
        transaction_fee = 0.0,
    )
    account.credit(amount)
    transaction.save()
    # TODO: Send mail to admin and customer
    return messages.success(request, 'Credit successful')
