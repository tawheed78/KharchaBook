from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewUserForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import AddExpenseForm
from .models import Profile, Expense
from django.db.models import Max
# from .models import User
# Create your views here.

def redirect_view(request):
    return redirect('login')

@login_required(login_url = 'login')
def home(request):
	try:
		profile = request.user.profile
		expenses = Expense.objects.filter(profile=profile).order_by('-id')
		top_five_expense = expenses[:5]
		income = profile.income if profile.income is not None else 0
		amounts = [int(expense.amount) for expense in expenses]
		total_expense = sum(amounts)
		# total_expense = sum(expense.amount for expense in expenses)
		balance = income - total_expense
	except Profile.DoesNotExist:
		profile = None
		income = 0
		total_expense = 0
		balance = 0
	context = {
		"income": income,
		"total_expense": total_expense,
		"balance":balance,
		"profile":profile,
		"expenses_count": expenses.count(),
		"top_five_expense":top_five_expense,
	}
	return render(request, 'home.html',context)



def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(reverse('login'))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "register.html", context={'form':form})


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are logged in")
				return redirect(reverse('home'))
			else:
				messages.error(request, "Invalid Username")
		else:
			messages.error(request, "Invalid Username")
	form = AuthenticationForm()
	context = {
		'login_form':form
    }
	return render(request, 'login.html',context)

@login_required(login_url = 'login')
def logout_view(request):
    logout(request)
    messages.info(request, "User Logout succesfully")
    return redirect('login')

@login_required(login_url = 'login')
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})


@login_required(login_url = 'login')
def add_expense(request):
	user_profile = Profile.objects.get(user=request.user)

	if request.method == 'POST':
		form = AddExpenseForm(request.POST)

		if form.is_valid():
			#create a new expense obj
			expense_id = Expense.objects.aggregate(Max('id'))['id__max'] + 1
			new_expense = form.save(commit=False)
			new_expense.id = expense_id
			new_expense.user = request.user
			new_expense.profile = user_profile
			new_expense.save()
			messages.success(request, "Expense added succesfully")
			return redirect(reverse('home'))
	else:
		form = AddExpenseForm()
	context = {
		"form":form,
	}
	return render(request, 'add_expense.html', context)

@login_required(login_url = 'login')
def update_expense(request, expense_id):
	expense = get_object_or_404(Expense, id=expense_id, user = request.user)
	if request.method == "POST":
		form = AddExpenseForm(request.POST, instance=expense)

		if form.is_valid():
			form.save()
			messages.success(request, "Expense updated succesfully")
			return redirect(reverse('home'))
	else:
		form = AddExpenseForm(instance=expense)
	
	context = {
		"form":form,
		"expense":expense,
		"expense_id":expense_id,
	}
	return render(request, 'update_expense.html', context)

@login_required(login_url = 'login')
def delete_expense(request, expense_id):
	expense = get_object_or_404(Expense, id = expense_id, user = request.user)
	expense.delete()
	# messages.WARNING("Expense deleted succesfully")
	return redirect(reverse('home'))
	

@login_required(login_url = 'login')
def expense_history(request):
	expense = Expense.objects.filter(user = request.user).order_by('-id')
	recent_expense = expense[:20]
	context = {
		"expense":expense,
		"expense_count":expense.count(),
		"recent_expense":recent_expense,
	}
	return render(request, 'expense_history.html', context)