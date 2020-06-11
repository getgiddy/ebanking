from django.urls import path
from core.views import (
    home,
    dashboard,
    transactions,
    profile,
    RegisterView,
    application_recieved,
    WithdrawalFormView,
    DepositFormView,
    TransferFormView,
)


urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/transactions/', transactions, name='transactions'),
    path('dashboard/deposit/', DepositFormView.as_view(), name='deposit'),
    path('dashboard/profile/', profile, name='profile'),
    path('dashboard/transfer/', TransferFormView.as_view(), name='transfer'),
    path('dashboard/withdraw/', WithdrawalFormView.as_view(), name='withdraw'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/application_recieved/', application_recieved, name='application-recieved'),
]
