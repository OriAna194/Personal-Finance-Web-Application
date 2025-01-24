from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default="RON")  

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    spent_amount = models.FloatField(default=0)
    created_on = models.DateField(auto_now_add=True)
    currency = models.CharField(max_length=3, default="RON")  

    def __str__(self):
        return self.title
