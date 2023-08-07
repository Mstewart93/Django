from django.forms import ModelForm
from .models import Account, Transaction


#create the form based on Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

#creates transaction form based on Transaction Model

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'