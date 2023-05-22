from django.db import models

from django.contrib.auth.models import User

from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db import models
class User(AbstractUser):
    username=models.CharField( max_length=50 ,null=True,unique=True)
   
    email=models.EmailField( max_length=254,null=True,unique=True)
    Mobile_number=models.CharField( max_length=50,null=True,blank=True)
    password=models.CharField( max_length=500,null=True,blank=True)
    confirm_password=models.CharField( max_length=50,null=True,blank=True)
  

    objects=UserManager()
    # USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
# class User_update(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_image = models.ImageField(default='img_569204.png', upload_to="users/",null=True,blank=True ) 


#    <!-- name , email , contact number , years of trading experience , whatsapp number , country -->
class contact_us_feedback(models.Model):
    c_name = models.CharField(max_length=50,null=True,blank=True)
    c_email = models.EmailField(max_length=254,null=True,blank=True)
    c_number = models.CharField( max_length=50 ,null=True,blank=True)
    c_experience=models.CharField( max_length=50,null=True,blank=True)
    c_wnumber=models.CharField( max_length=50,null=True,blank=True)
    c_country=models.CharField( max_length=50,null=True,blank=True)
    c_message=models.CharField( max_length=500,null=True,blank=True)
    def __str__(self):
        return self.c_name
    
  
    


    
  

    

