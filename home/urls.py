from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.redirect_view, name='root'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense_history/', views.expense_history, name='expense_history')
]