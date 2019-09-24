from django.db import models
from apps.login_reg.models import *
from apps.recipes.models import *

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    recipe = models.ManyToManyField(Recipe, related_name = "ingredients")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
