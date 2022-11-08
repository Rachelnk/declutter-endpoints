from rest_framework import serializers
from .models import *

class SellerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seller
    fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Buyer
    fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'

class SoldItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = SoldItem
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
