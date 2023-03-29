from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length = 50)
    about_me = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 1000)
    ability_types = models.ManyToManyField('AbilityType', through='Ability')

class Ability(models.Model):
    hero = models.ForeignKey('Hero', on_delete=models.PROTECT, null=True)
    ability_type = models.ForeignKey('AbilityType', on_delete=models.PROTECT, null=True)
    

class AbilityType(models.Model):
    name = models.CharField(max_length = 50, null=True)


class Relationship(models.Model):
    hero1 = models.ForeignKey('Hero', on_delete=models.PROTECT, null=True, related_name='hero1')
    hero2 = models.ForeignKey('Hero', on_delete=models.PROTECT, null=True, related_name='hero2')
    relationship_type = models.ForeignKey('RelationshipType', on_delete=models.PROTECT, null=True)

class RelationshipType(models.Model):
    name = models.CharField(max_length = 50, null=True)





