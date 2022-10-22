from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True )
  username = models.CharField(max_length=60)
  name = models.CharField(max_length=30)
  email= models.EmailField(blank=True)
  location= models.CharField(max_length=60, blank=False)
  contact=models.CharField(max_length=20, blank=False)

  def save_buyer(self):
    self.user()

  def delete_buyer(self):
    self.delete()

  # def get_posts(self):
  #   return

class Buyer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True )
  username = models.CharField(max_length=60)
  name = models.CharField(max_length=30)
  email= models.EmailField(blank=True)
  contact=models.CharField(max_length=20, blank=False)

  def save_buyer(self):
    self.user()

  def delete_buyer(self):
    self.delete()


