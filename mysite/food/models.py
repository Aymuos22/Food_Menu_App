from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
        
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=600,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdwTZ9RvEp9f8Twey_YzSo7q_fIt7T3bAe_SWMMozM_ZC2s1Kw4HaFGt7ozxoFL0R4D5k&usqp=CAU")
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    