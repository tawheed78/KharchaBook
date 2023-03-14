from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Expense, Profile

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class AddExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['name', 'amount', 'date']
		widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
	# def save(self, profile, commit=True):
	# 	expense = super().save(commit=False)
	# 	expense.profile = profile
	# 	if commit:
	# 		expense.save()
	# 	return expense
			


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['income']