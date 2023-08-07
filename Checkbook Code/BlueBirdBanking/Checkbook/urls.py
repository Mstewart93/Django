from django.urls import path
from . import views



urlpatterns = [
    #sets path to index.html
    path('', views.home, name='index'),
    #sets path to CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # sets path to BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    #sets path to AddNewTransaction.html
    path('transaction/',views.transaction, name='transaction')
]