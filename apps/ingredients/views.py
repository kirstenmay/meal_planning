from django.shortcuts import render, redirect, HttpResponse
from .models import Ingredient
from django.http import JsonResponse
from apps.recipes.models import *
from django.contrib import messages
import math


def ingredient(request):
    return render(request, 'Ingredients/Ingredients.html')


def add_ingredient(request):
    if 'userid' not in request.session:
        return redirect("/")
    errors = Ingredient.objects.ingredient_validator(request.POST) 
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/ingredients/')
    else:
        Ingredient.objects.create(name=request.POST['name'],description=request.POST['description'],price=request.POST['price'])
        return redirect('/ingredients/')

def find_recipe(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        'all_ingredients': Ingredient.objects.all(),
    }
    return render(request, 'ingredients/find_recipe.html', context)

def select_ingredient(request):
    string = ""
    choice = request.POST.getlist('ingredients[]')
    counter = 0
    for item in choice:
        counter += 1
        errors = Ingredient.objects.find_recipe_val(counter)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value, extra_tags=key)
                return JsonResponse({error: 403 })
        string += f"<li><input type='hidden' value='{item}' name = 'ingredient_{counter}'>{Ingredient.objects.get(id=item).name}</li>"
    return HttpResponse(string)

def dynamic_search(request):
    stuff = Ingredient.objects.filter(name__icontains=request.POST['srch'])
    strng = ""
    for thing in stuff:
        strng += f"<option value={thing.id}>{thing.name}</option>"
    return HttpResponse(strng)

def search_recipe(request):
    if 'userid' not in request.session:
        return redirect("/")
    ingredients =[]
    for stuff in request.POST:
        if stuff != 'csrfmiddlewaretoken' and stuff != 'srch':
            ingredients.append(Ingredient.objects.get(id = request.POST[stuff]))  
    matching_recipes = []
    for ingredient in ingredients:
        qs2 = Recipe.objects.filter(ingredients=ingredient)    
        for recipe in qs2:
            if recipe not in matching_recipes:
                matching_recipes.append(recipe)
    match_percentages = []
    for recipe in matching_recipes:
        counter = 0
        for ingredient in ingredients:
            if ingredient in recipe.ingredients.all():
                counter+=1
        match_percentages.append(math.floor((counter / len(ingredients))*100))
    all_things = []
    for i in range(len(matching_recipes)):
        all_things.append({ 'recipe': matching_recipes[i], 'percentage': match_percentages[i]})
    context = {
        'recipes': all_things, 
    }
    return render(request, 'ingredients/matched_recipes.html', context)