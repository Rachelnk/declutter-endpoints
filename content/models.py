from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True )
  username = models.CharField(max_length=60)
  name = models.CharField(max_length=30)
  email= models.EmailField(blank=True)
  location= models.CharField(max_length=60, blank=False)
  contact=models.CharField(max_length=20, blank=False)

  
