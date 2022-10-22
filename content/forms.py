from django import forms
from django import forms
from django.contrib.auth.models import User
from .models import Buyer, Seller, Item

class UpdateBuyerForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name', 'username', 'email']


class UpdateSellerForm(forms.ModelForm):
    # profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    contact = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Seller
        fields = ['location', 'contact']

class UpdateBuyerForm(forms.ModelForm):
    # profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    contact = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Buyer
        fields = ['contact']