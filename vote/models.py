from django.db import models
from datetime import date
from employee.models import Employee
from menu.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
