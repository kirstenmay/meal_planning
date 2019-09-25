from django.db import models
from apps.login_reg.models import *

class recipe_manager(models.Manager):
   def add_recipe_val(self, postData):
       errors = {}
       if len(postData['name']) < 3:
           errors['name'] = "A recipe name must be at least 3 characters"
       if len(postData['description']) < 3:
           errors['name'] = "A description must be provided"
       if len(postData['directions']) < 10:
           errors['directions'] = "Directions must be provided"
       if len(postData['ingredients[]']) < 1:
           errors['ingredients[]'] = "Ingredients must be added to post a new recipe"
       return errors

class Recipe(models.Model):
   name = models.CharField(max_length = 255)
   description = models.TextField()
   directions = models.TextField()
   creator = models.ForeignKey(User, related_name = "recipe_creator")
   recipe_users = models.ManyToManyField(User, related_name = "recipes_tried")
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   objects = recipe_manager()

class review_manager(models.Manager):
   errors = {}
   def add_review_val(self, postData):
       if len(postData['review']) < 10:
           errors['review'] = "Review must be at least 10 characters long"
       return errors
       
class Review(models.Model):
   review = models.TextField()
   user = models.ForeignKey(User, related_name = "review")
   recipe = models.ForeignKey(Recipe, related_name = "review")
   created_at = models.DateTimeField(auto_now_add=True)
   udpated_at = models.DateTimeField(auto_now=True)
   objects = review_manager()
