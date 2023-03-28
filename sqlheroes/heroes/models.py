from django.db import models

# Create your models here.
class Heroes(models.Model):
    name = models.CharField(max_length=50)
    about_me = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)

#class Ability_Types(models.Model):
    #pass

#class Relationship_Types(models.Model):
    #pass

