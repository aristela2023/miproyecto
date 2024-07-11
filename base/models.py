from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Posts(models.Model):
   title = models.CharField(max_length=200)
   text= models.TextField()
   updated = models.DateTimeField(auto_now= True)
   created =models.DateTimeField(auto_now_add= True)
   user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
   
   def _str_(self):
       return self.title 
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now= True)
    created =models.DateTimeField(auto_now_add= True)

