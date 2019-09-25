from django.shortcuts import render, redirect
from .models import Ingredient
from django.contrib import messages
def ingredient(request):
    return render(request, 'Ingredients/Ingredients.html')
def add_ingredient(request):
    errors = Ingredient.objects.ingredient_validator(request.POST) 
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/ingredients/')
    else:
        Ingredient.objects.create(name=request.POST['name'],description=request.POST['description'],price=['price'])
        return redirect('/ingredients/')
