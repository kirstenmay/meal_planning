from django.db import models
from apps.login_reg.models import *
from apps.recipes.models import *

class IngredientMananger(models.Manager):
    def ingredient_validator(self, postData):
        errors = {}
        price = postData['price']
        if len(postData['name']) < 2:
            errors['name'] = 'Ingredient name must be at least 2 characters long'
        if len(postData['description']) < 5:
            errors['description'] = 'Description must be at least 5 characters long'
        if  type(price) is not int:
            errors['price']= 'Price must be a number'
        return errors
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    recipe = models.ManyToManyField(Recipe, related_name = "ingredients")
    objects= IngredientMananger()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
