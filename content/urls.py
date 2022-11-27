from django.urls import re_path, path
from .views import *
# from . import views
from content import views
from rest_framework_jwt.views import (obtain_jwt_token, verify_jwt_token, refresh_jwt_token)

urlpatterns = [
  path('', views.index, name='index'),

  # users endpoints
  path('users/', views.UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', views.UserDetail.as_view(), name='user-details'),

  # item endpoints
  path('api/items/', views.ItemList.as_view()),
  path('api/item-details/<int:pk>/', views.ItemDetails.as_view()),

  # buyer endpoints
  path('api/buyers/', views.BuyerList.as_view()),
  path('api/buyer-details/<int:pk>', views.BuyerDetail.as_view()),

  # seller endpoints
  path('api/sellers/', views.SellerList.as_view()),
  path('api/seller-details/<int:pk>', views.SellerDetail.as_view()),

  # sold items endpoints
  path('api/sold-items/', views.SoldItemList.as_view()),
  path('api/solditem-details/<int:pk>', views.SoldItemDetail.as_view()),


  # login signup endpoints
  path('signin/', GetTokenPairView.as_view(), name='token_obtain_pair'),
  path('signup-seller/', RegisterSellerView.as_view(), name='signup-seller'),
  path('signup-buyer/', RegisterBuyer.as_view(), name='signup-buyer'),
  re_path(r'^login', views.LoginUser.as_view()),
  re_path(r'^token_auth', obtain_jwt_token),
  re_path(r'^refresh_token', refresh_jwt_token),
  re_path(r'^verify_token', verify_jwt_token),
  
  
]
