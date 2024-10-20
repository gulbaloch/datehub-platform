from django import forms
from .models import User

class User_forms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'last_name', 'email','profile_image']
       

   