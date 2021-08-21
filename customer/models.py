from django.db import models
from django.db.models import Q

class Books(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=64)
  status = models.PositiveIntegerField()
  price = models.PositiveIntegerField()
  contact = models.TextField()

# Create your models here.
