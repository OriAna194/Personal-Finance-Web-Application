from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, Category
from .forms import GoalForm, CategoryForm


def home(request):
    goals = Goal.objects.all()
    total_saved = sum(goal.saved_amount for goal in goals)
    goal_data = []

    for goal in goals:
        
        if goal.target_amount > 0:
            percentage_saved = (goal.saved_amount / goal.target_amount) * 100
        else:
            percentage_saved = 0
        goal_data.append({
            'goal': goal,
            'percentage_saved': percentage_saved
        })

    return render(request, 'home.html', {'goals': goals, 'goal_data': goal_data, 'total_saved': total_saved})



def expenses(request):
    categories = Category.objects.all()
    return render(request, 'expenses.html', {'categories': categories})


def addGoal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GoalForm()
    return render(request, 'addGoal.html', {'form': form})


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
            form.save()
            return redirect('expenses')
    else:
        form = CategoryForm()
    return render(request, 'addCategory.html', {'form': form})


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