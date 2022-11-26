from django.urls import re_path, path, url
from .views import *
from . import views
from rest_framework_jwt.views import (obtain_jwt_token, verify_jwt_token, refresh_jwt_token)

urlpatterns = [
  path('', views.index, name='index'),

  # users endpoints
  path('users/', views.UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', views.UserDetail.as_view(), name='user-details'),

  # seller endpoints
  path('api/items/', views.ItemList.as_view()),
  path('api/items/<int:pk>/', views.ItemDetails.as_view()),


  # buyer endpoints


  # items endpoints

  # sold items endpoints

  # login signup endpoints
  path('signin/', GetTokenPairView.as_view(), name='token_obtain_pair'),
  path('signup-seller/', RegisterSellerView.as_view(), name='signup-seller'),
  path('signup-buyer/', RegisterBuyer.as_view(), name='signup-buyer'),
  url(r'^login', views.LoginUser.as_view()),
  url(r'^token_auth', obtain_jwt_token),
  url(r'^refresh_token', refresh_jwt_token),
  url(r'^verify_token', verify_jwt_token),
  url(r'^'),
  
]
