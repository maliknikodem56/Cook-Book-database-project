

from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Diet(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=150)
    dish_type = models.ForeignKey("DishType", on_delete=models.SET_NULL, null=True, blank=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.SET_NULL, null=True, blank=True)
    diet = models.ForeignKey("Diet", on_delete=models.SET_NULL, null=True, blank=True)
    kcal_per_100g = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField()
    preparation_time_minutes = models.IntegerField()

    def __str__(self):
        return self.name
