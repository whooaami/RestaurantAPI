from django.db import models
from datetime import date
from employee.models import Employee
from restaurant.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dishes = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    prices = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"Dish is {self.dishes} for {self.prices} on {self.date}"
