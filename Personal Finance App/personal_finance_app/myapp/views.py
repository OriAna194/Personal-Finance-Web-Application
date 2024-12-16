from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, Category
from .forms import GoalForm, CategoryForm
from django.http import JsonResponse
from .utils import get_conversion_rate


from decimal import Decimal

def home(request):
    goals = Goal.objects.all()
    total_saved = sum(goal.saved_amount for goal in goals)

    # Get the currency from the query parameters, default to 'RON'
    selected_currency = request.GET.get('currency', 'RON')

    # Fetch the conversion rate for the selected currency
    if selected_currency == 'RON':
        conversion_rate = Decimal(1)  # Base currency
    else:
        conversion_rate = Decimal(get_conversion_rate('RON', selected_currency))

    # Convert total saved to the selected currency
    converted_total_saved = total_saved * conversion_rate

    goal_data = []
    for goal in goals:
        # Convert goal amounts to the selected currency
        converted_saved_amount = goal.saved_amount * conversion_rate
        converted_target_amount = goal.target_amount * conversion_rate

        if goal.target_amount > 0:
            percentage_saved = (goal.saved_amount / goal.target_amount) * 100
        else:
            percentage_saved = 0

        # Add converted values to goal data
        goal_data.append({
            'goal': goal,
            'percentage_saved': percentage_saved,
            'converted_saved_amount': converted_saved_amount,
            'converted_target_amount': converted_target_amount,
        })

    return render(request, 'home.html', {
        'goal_data': goal_data,
        'total_saved': converted_total_saved,  # Pass the converted total saved
        'selected_currency': selected_currency,  # Pass selected currency
    })







def expenses(request):
    categories = Category.objects.all()

    # Get selected currency and conversion rate
    selected_currency = request.GET.get('currency', 'RON')
    conversion_rate = get_conversion_rate('RON', selected_currency)

    # Convert spent amounts
    for category in categories:
        category.converted_spent_amount = category.spent_amount * conversion_rate

    return render(request, 'expenses.html', {
        'categories': categories,
        'selected_currency': selected_currency,
    })



def addGoal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            # Save the goal with the selected currency
            goal = form.save(commit=False)
            goal.currency = request.POST.get('currency', 'RON')
            goal.save()
            return redirect('home')
    else:
        form = GoalForm()
    return render(request, 'addGoal.html', {
        'form': form,
        'currencies': ['RON', 'EUR', 'USD', 'JPY', 'KRW', 'HUF'],
    })


def updateGoal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)  

    if request.method == 'POST':
        
        new_saved_amount = request.POST.get('newSavedAmount')
        if new_saved_amount:
            new_saved_amount = float(new_saved_amount)  

            goal.saved_amount += new_saved_amount
            goal.save()  

        return redirect('home')  
    else:
        
        return render(request, 'updateGoal.html', {'goal': goal})


def deleteGoal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    return redirect('home')


def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Save the category with the selected currency
            category = form.save(commit=False)
            category.currency = request.POST.get('currency', 'RON')
            category.save()
            return redirect('expenses')
    else:
        form = CategoryForm()
    return render(request, 'addCategory.html', {
        'form': form,
        'currencies': ['RON', 'EUR', 'USD', 'JPY', 'KRW', 'HUF'],
    })


def updateCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)  

    if request.method == 'POST':

        new_spent_amount = request.POST.get('newSpentAmount')
        if new_spent_amount:
            new_spent_amount = float(new_spent_amount)  

            
            category.spent_amount += new_spent_amount
            category.save()  

        return redirect('expenses')  
    else:
        return render(request, 'updateCategory.html', {'category': category})


def deleteCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('expenses')


def reset_expenses(request):
    if request.method == 'POST':  
        Category.objects.update(spent_amount=0)  
        return redirect('expenses') 
    



def convert_currency(request):
    selected_currency = request.GET.get('currency', 'RON')
    rates = {
        'EUR': get_conversion_rate('RON', 'EUR'),
        'USD': get_conversion_rate('RON', 'USD'),
        'JPY': get_conversion_rate('RON', 'JPY'),
        'KRW': get_conversion_rate('RON', 'KRW'),
        'HUF': get_conversion_rate('RON', 'HUF'),
    }

    # Prepare a dictionary for conversion
    converted_values = {key: rates.get(selected_currency) for key in rates}
    return JsonResponse(converted_values)    