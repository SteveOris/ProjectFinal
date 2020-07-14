from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Album(models.Model):
  artist_name = models.CharField(max_length=255,null=True, blank=True)
  title = models.CharField(max_length=255,null=True, blank=True)
  date_released = models.DateField(null=True, blank=True)

  def __str__(self):
    return f'{self.title}'