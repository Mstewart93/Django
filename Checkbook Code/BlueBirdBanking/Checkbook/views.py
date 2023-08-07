from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Create your views here.


#lets you renderthe homepage
def home(request):
    form = TransactionForm(data=request.POST or None) #retreives form
    #checksif request method is POST
    if request.method == 'POST':
        pk = request.POST['account']#if form is submited retreive witch account they want
        return balance(request, pk)#call balance function that accounts balance sheet
    content = {'form': form} #pass content to the template in a dictionary
    #adds content of form to page 
    return render(request, 'checkbook/index.html', content)

#renders the create new account page
def create_account(request):
    form = AccountForm(data=request.POST or None) #retreive account form
    #checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #check to see if the submitted form is valid saves it
            form.save() # saves new content
            return redirect('index') #returns user back to the homepage
    content = {'form': form} #saves content to the template as a dictionary
    #adds content of form to the page 
    return render(request, 'checkbook/CreateNewAccount.html', content)

#renders the blance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #retreive the account using primary key
    transactions = Transaction.Transactions.filter(account=pk)# retreive all transactions
    current_total = account.initial_deposit #create account total varaiable
    table_contents = {} #create a dictionary into which the transactin info will be place
    for t in transactions: #loop through transactions and determine which is a deposit or withdrawl
        if t.type == 'Deposit':
            current_total += t.amount 
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
        
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

#renders the transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)#get the form
    #checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #checks to see if form is valid if so saves it
            pk = request.POST['account']
            form.save() #saves
            return balance(request,pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
