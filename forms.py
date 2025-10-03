from django import forms
from .models import Dish, Cuisine, DishType, Diet

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

class CuisineForm(forms.ModelForm):
    class Meta:
        model = Cuisine
        fields = "__all__"

class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"

class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = "__all__"
