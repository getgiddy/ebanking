from django.urls import path
from core.views import (
    home,
    dashboard,
    transactions,
    deposit,
    profile,
    transfer,
    withdraw,
    RegisterView,
    application_recieved,
)


urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/transactions/', transactions, name='transactions'),
    path('dashboard/deposit/', deposit, name='deposit'),
    path('dashboard/profile/', profile, name='profile'),
    path('dashboard/transfer/', transfer, name='transfer'),
    path('dashboard/withdraw/', withdraw, name='withdraw'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/application_recieved/', application_recieved, name='application-recieved'),
]
