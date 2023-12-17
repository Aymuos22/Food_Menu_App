from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profilepictures')
    location=models.CharField(max_length=500)
    desc=models.CharField(max_length=500,default='')
    
    def __str__(self):
        return self.user.username