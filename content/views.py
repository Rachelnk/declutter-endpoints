from django.shortcuts import render, redirect
from django.http.response import Http404, HttpResponse
from .serializer import *
from .serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
# import requests
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
from declutter.settings import SECRET_KEY

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from declutter import settings
from .models import Seller, Item, SoldItem, Buyer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()


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

class SoldItemList(APIView):
  permission_classes= (AllowAny, )

  def get(self, request):
    solditems = SoldItem.objects.all()
    serializer = SoldItemSerializer(solditems, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = SoldItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SoldItemDetail(APIView):
  permission_classes = (AllowAny, )

  def get_object(self, pk):
    try:
      return SoldItem.objects.get(pk=pk)
    except SoldItem.DoesNotExist:
      raise Http404 
  
  def get(self, request, pk, format=None):
    solditem = self.get_object(pk)
    serializer = SoldItemSerializer(solditem)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    solditem = self.get(pk)
    serializer = SoldItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk, format=None):
    solditem=self.get_object(pk)
    solditem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BuyerList(APIView):
  permission_classes= (AllowAny, )

  def get(self, request):
    buyers = Buyer.objects.all()
    serializer = BuyerSerializer(buyers, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = BuyerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerDetail(APIView):
  permission_classes = (AllowAny, )
  
  def get_object(self, pk):
    try:
      return Buyer.objects.get(pk=pk)
    except Buyer.DoesNotExist:
      raise Http404  

  def get(self, pk, request, format=None):
    buyer = self.get_object(pk)
    serializer = BuyerSerializer(buyer)
    return Response(serializer.data)  

  def put(self, request, pk, format=None):
    buyer = self.get_object(pk)
    serializer = BuyerSerializer(buyer, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # delete solditem
  def delete(self, request, pk, format=None):
    buyer = self.get_object(pk)
    buyer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class SellerList(APIView):
  permission_classes= (AllowAny, )

  def get(self, request):
    sellers = Seller.objects.all()
    serializer = SellerSerializer(sellers, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = SellerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerDetail(APIView):
  permission_classes = (AllowAny, )
  
  def get_object(self, pk):
    try:
      return Seller.objects.get(pk=pk)
    except Seller.DoesNotExist:
      raise Http404  

  def get(self,request ,pk, format=None):
    seller = self.get_object(pk)
    serializer = SellerSerializer(seller)
    return Response(serializer.data)  

  def put(self, request, pk, format=None):
    seller = self.get_object(pk)
    serializer = SellerSerializer(seller, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # delete solditem
  def delete(self, request, pk, format=None):
    seller = self.get_object(pk)
    seller.delete()
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
  serializer_class= RegisterBuyerSerializer

# items list
@api_view(['GET', 'POST','DELETE'])
def item_list(request, seller_id):
    try:
      sellers = Seller.objects.get(id=seller_id)
      items = Item.objects.filter(seller_id=sellers)
    except Item.DoesNotExist:
      return JsonResponse({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':      
      items_serializer=ItemSerializer(items, many=True, context={'request': request})
      return Response(items_serializer.data)
    elif request.method == 'POST':
      items_data= JSONParser().parse(request)
      items_serializer = ItemSerializer(data=items_data)
      if items_serializer.is_valid():
        items_serializer.save(seller_id=seller_id)
        return Response(items_serializer.data, status=status.HTTP_201_CREATED)
      return Response(items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request == 'DELETE':
      items.delete()
      return JsonResponse({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    


# single item view
@api_view(['GET', 'PUT'])
def item_details(request, item_id):
  try:
    item = Item.objects.get(id=item_id)
  except Item.DoesNotExist:
    return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    item_serializer = ItemSerializer(item, many=True)
    return Response(item_serializer.data)
  elif request.method == 'PUT':
    item_data = JSONParser().parse(request)
    item_serializer= ItemSerializer(item, data=item_data)
    if item_serializer.is_valid():
      item_serializer.save()
      return JsonResponse(item_serializer.data)
    return JsonResponse(item_serializer.errors, status=status.HTTP_404_NOT_FOUND)

# post sold item
@api_view(['POST', 'GET'])
def sold_item(request, item_id):
  # try:
  #   sellers=Seller.objects.get()
  # except:
  if request.method == 'POST':
    solditem_data=JSONParser().parse(request)
    solditem_serializer= SoldItemSerializer(data=solditem_data)
    if solditem_serializer.is_valid():
      solditem_serializer.save()
      return Response(solditem_serializer.data, status=status.HTTP_201_CREATED)
    return Response(solditem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  # if request.method == 'GET':

# get sold items view
@api_view(['GET', 'DELETE'])
def bought_item(request, buyer_id):
  try:
    buyer = Buyer.objects.get(id=buyer_id)
    sold_item = SoldItem.objects.filter(id=buyer)
  except SoldItem.DoesNotExist:
    return JsonResponse({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    sold_serializer = SoldItemSerializer(sold_item, many=True)
    return Response(sold_serializer.data)
  elif request.method == 'DELETE':
    sold_serializer.delete()
    return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class LoginUser(APIView):
  permission_classes = (AllowAny, )
  def post(self, request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      payload = jwt_payload_handler(user)
      return Response({
        'id':user.id,
        'response_code':'success',
        'response_msg':'Login Successful',
        'username':user.username,
        'token':jwt.encode(payload, SECRET_KEY)
      }, status.HTTP_200_OK)
    else:
      return Response(
        { 'response_code':'error',
          'response_msg':'Invalid credentials'}, status.HTTP_400_BAD_REQUEST
          )

# @api_view(['GET'])
# @permission_classes((AllowAny))



    











