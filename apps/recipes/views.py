from django.shortcuts import render, redirect, HttpResponse
from apps.login_reg.models import *
from apps.ingredients.models import *

def new_recipe(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        'ingredients': Ingredient.objects.all()
    }
    return render(request, 'recipes/new_recipe.html', context)

def add_recipe(request):
    if 'userid' not in request.session:
        return redirect("/")
    # errors = Job.objects.new_job_val(request.POST)
    #     if len(errors) > 0:
    #         for key, value in errors.items():
    #             messages.error(request, value, extra_tags=key)
    #         return redirect("/add_job")
    recipe = Recipe.objects.create(name = request.POST['name'], description = request.POST['description'], directions = request.POST['directions'])
    options = request.POST.getlist('ingredients[]')
    for i in options:
        this_ingredient = i
        ingredient = Ingredient.objects.get(id= this_ingredient)
        this_recipe = Recipe.objects.get(id=recipe.id)
        this_recipe.ingredients.add(ingredient)
    return redirect("/success")
