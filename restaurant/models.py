from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Restaurant name is {self.name}"
