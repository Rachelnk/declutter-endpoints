from django.shortcuts import render, redirect
from django.http.response import Http404, HttpResponse
from .serializer import *
from .serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics

import requests
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import responses
from rest_framework import status

from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework_jwt.settings import api_settings
import jwt
import json
# from settings import SECRET_KEY

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from declutter import settings
from .models import Seller, Item, SoldItem, Buyer
from rest_framework import Response
from rest_framework.views import APIView


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

def index (request):
  return HttpResponse ('Welcome to Declutter254')

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_classes = UserSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
      user = User.objects.filter(id=pk).first()
      serializer = UserSerializer(user)
      return Response(serializer.data)

# items
class ItemList(APIView):
  permission_classes = (AllowAny,)

  def get(self, request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, format=None):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetails(APIView):
   permission_classes= (AllowAny,)

   def get_object(self, pk):
    try:
      item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
      raise Http404

  # get a particular item
   def get(self, request, pk, format=None):
      item = self.get_object(pk)
      serializer = ItemSerializer(item)
      return Response(serializer.data)

  # update a particular item
   def put(self, request, pk, format=None):
      item = self.get_object(pk)
      serializer = ItemSerializer(item, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # delete item
   def delete(self, request, pk, format=None):
    item = self.get_object(pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class SoldItem(APIView):
  permission_classes = (AllowAny, )

  def get(self, request):
    solditem = SoldItem.objects.all()
    serializer = SoldItemSerializer(solditem, many=True)
    return Response(serializer.data)

  
  def post(self, request):
    serializer = SoldItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SoldItemDetails(APIView):
  permission_classes = (AllowAny, )
  
  def get_object(self, pk):
    try:
      return SoldItem.objects.get(pk=pk)
    except SoldItem.DoesNotExist:
      raise Http404

  # get particular solditem

  def get(self, pk, request, format=None):
    solditem = self.get_object(pk)
    serializer = SoldItemSerializer(solditem)
    return Response(serializer.data)

  # update solditem

  def update(self, request, pk, format=None):
    solditem = self.get_object(pk)
    serializer = SoldItemSerializer(solditem, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # delete solditem
  def delete(self, request, pk, format=None):
    solditem = self.get_object(pk)
    solditem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# get login token
class GetTokenPairView(TokenObtainPairView):
  permission_classes=(AllowAny, )
  serializer_class= GetTokenPairSerializer

# register seller
class RegisterSellerView(generics.CreateAPIView):
  queryset= User.objects.all()
  permission_classes=(AllowAny, )
  serializer_class= RegisterSellerSerializer

# register buyer
class RegisterBuyer(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes=(AllowAny, )
  serializer_class=RegisterBuyerSerializer

















