from django.db import models

# Create your models here.


class Posts(models.Model):
   title = models.CharField(max_length=200)
   text= models.TextField()
   updated = models.DateTimeField(auto_now= True)
   created =models.DateTimeField(auto_now_add= True)
   def _str_(self):
       return self.title 
    