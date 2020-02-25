# hospitalapp/forms.py

from django import forms
from .models import Menu
from django.contrib.auth import get_user_model

class CreateMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'status' , 'id_parent']


User = get_user_model()

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'address', 'dob', 'gender', 'about')