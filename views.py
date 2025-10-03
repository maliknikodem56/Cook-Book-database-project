

import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, DishType, Cuisine, Diet
from .forms import DishForm, CuisineForm, DishTypeForm, DietForm

def dishes_list(request):
    dish_type_id = request.GET.get("dish_type")
    cuisine_id = request.GET.get("cuisine")
    diet_id = request.GET.get("diet")
    search_query = request.GET.get("search")
    random_request = request.GET.get("random")

    dishes = Dish.objects.all()

    if dish_type_id:
        dishes = dishes.filter(dish_type_id=dish_type_id)
    if cuisine_id:
        dishes = dishes.filter(cuisine_id=cuisine_id)
    if diet_id:
        dishes = dishes.filter(diet_id=diet_id)
    if search_query:
        dishes = dishes.filter(name__icontains=search_query)

    random_dish = None
    if random_request == "1" and dishes.exists():
        random_dish = random.choice(list(dishes))

    context = {
        "dishes": dishes,
        "dish_types": DishType.objects.all(),
        "cuisines": Cuisine.objects.all(),
        "diets": Diet.objects.all(),
        "selected_dish_type": dish_type_id or "",
        "selected_cuisine": cuisine_id or "",
        "selected_diet": diet_id or "",
        "search_query": search_query or "",
        "random_dish": random_dish,
    }
    return render(request, "Cookbook/dishes_list.html", context)

def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dishes_list")
    else:
        form = DishForm()
    return render(request, "Cookbook/add_dish.html", {"form": form})

def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect("dishes_list")
    else:
        form = DishForm(instance=dish)
    return render(request, "Cookbook/edit_dish.html", {"form": form})

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == "POST":
        dish.delete()
        return redirect("dishes_list")
    return render(request, "Cookbook/delete_dish.html", {"dish": dish})

def add_cuisine(request):
    if request.method == "POST":
        form = CuisineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dishes_list")
    else:
        form = CuisineForm()
    return render(request, "Cookbook/add_cuisine.html", {"form": form})

def add_dish_type(request):
    if request.method == "POST":
        form = DishTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dishes_list")
    else:
        form = DishTypeForm()
    return render(request, "Cookbook/add_dish_type.html", {"form": form})

def add_diet(request):
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dishes_list")
    else:
        form = DietForm()
    return render(request, "Cookbook/add_diet.html", {"form": form})

def delete_cuisine(request, cuisine_id):
    cuisine = get_object_or_404(Cuisine, pk=cuisine_id)
    if request.method == "POST":
        cuisine.delete()
        return redirect("dishes_list")
    return render(request, "Cookbook/delete_cuisine.html", {"cuisine": cuisine})

def delete_dish_type(request, type_id):
    dish_type = get_object_or_404(DishType, pk=type_id)
    if request.method == "POST":
        dish_type.delete()
        return redirect("dishes_list")
    return render(request, "Cookbook/delete_dish_type.html", {"dish_type": dish_type})

def delete_diet(request, diet_id):
    diet = get_object_or_404(Diet, pk=diet_id)
    if request.method == "POST":
        diet.delete()
        return redirect("dishes_list")
    return render(request, "Cookbook/delete_diet.html", {"diet": diet})