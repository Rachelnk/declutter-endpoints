from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class User(AbstractUser):
  is_seller = models.BooleanField(default=False)
  is_buyer = models.BooleanField(default=False)

STATUS = [
('Sold',('Sold')),
('In Stock',('In Stock')),
]

COUNTIES = [
  ('Nairobi',('Nairobi')),
  ('Nakuru',('Nakuru')),
  ('Mombasa',('Mombasa')),
  ('Kisumu',('Kisumu')),
  ('Kiambu',('Kiambu')),
  ('Eldoret',('Eldoret')),
]
class Seller(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True )
  username = models.CharField(max_length=60)
  name = models.CharField(max_length=30)
  email= models.EmailField(blank=True)
  location= models.CharField(max_length=60, blank=False)
  contact=models.IntegerField()
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)


  def __str__(self):
    return str(self.user)

  def save_seller(self):
    self.user()

  def delete_seller(self):
    self.delete()

  class Meta: 
      verbose_name_plural = 'Seller'

  # def get_posts(self):
  #   return

class Buyer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True )
  username = models.CharField(max_length=60)
  name = models.CharField(max_length=30)
  email= models.EmailField(blank=True)
  contact=models.IntegerField()
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)

  def __str__(self):
    return str(self.user)

  def save_buyer(self):
    self.user()

  def delete_buyer(self):
    self.delete()

  class Meta: 
      verbose_name_plural = 'Buyer'

class Item(models.Model):
  seller_id=models.ManyToManyField(Seller, blank=False)
  name = models.CharField(max_length=30)
  image = CloudinaryField('image')
  description = models.CharField(max_length=140)
  selling_price = models.IntegerField()
  buying_price = models.IntegerField()
  age = models.IntegerField()
  status = models.CharField(max_length=30, choices=STATUS)
  county = models.CharField(max_length=30, choices=COUNTIES )
  location= models.CharField(max_length=60, blank=False)
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)
  updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated, ', null=True)

def __str__(self):
  return str(self.name)

def delete_item(self):
  self.delete()

def save_item(self):
  self.save()

class Meta:
  verbose_name_plural = 'Items'

class SoldItem(models.Model):
  item= models.ManyToManyField(Item, blank=True)
  buyer=models.ManyToManyField(Buyer, blank=True)
  created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)

  def delete_soldItem(self):
    self.delete()

  def save_soldItem(self):
    self.save()

class Meta:
  verbose_name_plural = 'Sold Item'




