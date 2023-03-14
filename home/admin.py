from django.contrib import admin
from .models import Expense, Profile
# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display=("user","name","amount","date")

admin.site.register(Expense, ExpenseAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=("user","income")

admin.site.register(Profile, ProfileAdmin )
