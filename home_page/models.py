from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)  
    password = models.CharField(max_length=40)
    profile_image = models.ImageField(upload_to='profile_images/')  
    date_of_join = models.DateField(_("Date of Joining"), auto_now_add=True) 

class Stores(models.Model):
    store_id = models.CharField(max_length=30, primary_key=True)
    store_name = models.CharField(max_length=30, blank=False, null=True)  
    store_description = models.CharField(max_length=100)
    store_logo = models.ImageField(upload_to='store_logos/') 
    store_creation_date = models.DateField(_("Date of Creation"), auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store' ,default=None)  # One-to-one relationship

    def __str__(self):
        return self.store_name
    


