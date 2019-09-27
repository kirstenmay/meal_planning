from django.db import models
from apps.recipes.models import *

class IngredientMananger(models.Manager):
    def ingredient_validator(self, postData):
        errors = {}
        price = postData['price']
        if len(postData['name']) < 2:
            errors['name'] = 'Ingredient name must be at least 2 characters long'
        if len(postData['description']) < 5:
            errors['description'] = 'Description must be at least 5 characters long'
        try:
            if float(price) < 0:
                errors['price'] = "Price can not be less than 0"
        except:
            errors['price']= 'Price must be a number'
        return errors

    def find_recipe_val(self, counter):
        errors = {}
        if counter > 8:
            errors['ingredients'] = "You can only add up to 8 ingredients"
        return errors
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    recipe = models.ManyToManyField(Recipe, related_name = "ingredients")
    objects= IngredientMananger()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
