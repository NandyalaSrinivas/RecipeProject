from django.db import models


class RecipeModel(models.Model):
    recipename= models.CharField(max_length=100)
    ingredients= models.CharField(max_length=500)
    making= models.CharField(max_length=500)
    recipepic= models.ImageField(upload_to = 'images/')
