from django.shortcuts import render, redirect, HttpResponse
from apps.login_reg.models import *
# from apps.Ingredients.models import *

def new_recipe(request):
    context = {
        # 'ingredients': Ingredients.objects.all()
    }
    return render(request, 'recipes/new_recipe.html', context)

def add_recipe(request):
    return redirect("/success")
