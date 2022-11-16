from dataclasses import field
from readline import get_current_history_length
from urllib import response
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator 
from django.contrib.auth.password_validation import validate_password
from .models import *
from .models import AbstractUser
from rest_framework.response import Response
from .serializer import *

# get user token

class GetTokenPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token= super(GetTokenPairSerializer,cls).get_token(user)

    token['username'] = user.username
    print(user.is_seller)
    return token

# register seller
class RegisterSellerSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('name', 'username','password1','password2')

  extra_kwargs = {
    'name': {'required': True}
  }

  def validate(self, attrs):
    if attrs['password1'] != attrs['password2']:
      raise serializers.ValidationError({"password1": "Password fields didn't match."})

    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      name=validated_data['name'],
      is_seller=True
    )

    user.set_password(validated_data['password1'])
    user.is_seller =True
    user.save()
    return user


# register buyer serializer

class RegisterBuyerSerializer(serializers.ModelSerializer):
  email=serializers.EmailField(required=True, validators=[UniqueValidator(User.objects.all())])
  password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = Buyer
    fields= ('name','username','email','password1', 'password2')
    extra_kwargs={'name': {'required':True}}

  def validate(self, attrs):
    if attrs['password1'] != attrs['password2']:
      raise serializers.ValidationError({"password1":"Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      name=validated_data['name'],
      email=validated_data['email'],
      is_buyer=True
    )
    user.set_password(validated_data['password1'])
    user.is_buyer=True
    user.save()

    return user

class RegisterItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields= ['__all__']

class RegisterItemUpdateSerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    return ItemSerializer(instance).to_representation(instance)

  class Meta:
    model = Item
    fields = ['__all__']


class RegisterSoldItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = SoldItem
    fields = ['__all__']

  