from django import forms
from .models import Goal, Category

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'target_amount', 'saved_amount']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'spent_amount']
