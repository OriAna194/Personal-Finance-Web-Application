from django import forms
from .models import Goal, Category

CURRENCY_CHOICES = [
    ('RON', 'Romanian Leu'),
    ('EUR', 'Euro'),
    ('USD', 'US Dollar'),
    ('JPY', 'Japanese Yen'),
    ('KRW', 'South Korean Won'),
    ('HUF', 'Hungarian Forint'),
]

class GoalForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, required=True)

    class Meta:
        model = Goal
        fields = ['title', 'target_amount', 'saved_amount']


class CategoryForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, required=True)

    class Meta:
        model = Category
        fields = ['title', 'spent_amount', 'currency']
