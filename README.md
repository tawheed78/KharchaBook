# KharchaBook
The KharchaBook is basically an Expense Tracker made completely by backend development in Django.
The app starts with an authentication method which provides User to Register in the database, as soon as the user is registered it takes the User to Login Page.
After the authentication succeeds a Home Page appears showing default values of income and expense.
User can go to profile and add his/her income to reflect in home page.
The app has Home, Add Expense, Expense History, Profile and Logout options in the navbar.
Home => Homepage
Add Expense => To add a new expense (It shows the five latest expenses only)
Expense History => Shows all the transactions (I have set it to 20 latest expenses)
Profile => To add Income details ( Will work on it to add more fields to models.py to take user input in profile updation)
Logout => Takes back to login page
As soon as any expense is added the views.py performs the functions and the data is rendered in the Home page by adding the expense value in expenses and Subtracting the same value from "Your Balance"
Your Balance shows the (Income - Expenditure ) balance available.
No major attention is given to the UI as the project was more focussed towards implementing Backend logics

#Updates to be done
1) Adding the option to update or delete any expense.
2) Adding more fields to the Profile Model
3) Adding alert message while adding, updating or deleting any expense

Will update if there  is more to it...
