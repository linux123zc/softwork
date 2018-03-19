from django.db import models

# Create your models here.
#coding:utf-8

class User(models.Model):
   username = models.CharField(max_length = 32)
   password = models.CharField(max_length = 32)
