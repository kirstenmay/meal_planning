from django.db import models
from apps.login_reg.models import *

class Recipe(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    directions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name = "review")
    recipe = models.ForeignKey(Recipe, related_name = "review")
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
