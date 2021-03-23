from django.db import models

# Create your models here.

class Item(models.Model):
    hint = models.CharField(max_length=400)
    id = models.IntegerField(primary_key=True)
    img = models.CharField(max_length=100)
    dname = models.CharField(max_length=100)
    qual = models.CharField(max_length=100)
    cost = models.IntegerField(null=True)
    notes = models.CharField(max_length=100)
    mc = models.CharField(max_length=10)
    lore = models.CharField(max_length=100)
    cd = models.IntegerField()
    components = models.CharField(max_length=100,null=True)
    created = models.BooleanField()
    charges = models.CharField(max_length=10)
    attrib = models.JSONField()
    # attrib = models.CharField(max_length=200)
    #rare
    desc = models.CharField(max_length=10,null=True)
    tier = models.IntegerField(null=True)