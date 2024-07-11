from django.urls import path
from django.urls import path, include
from . import views
#from base import views        

urlpatterns = [
     #path('', include('base.urls')),
     #path('api/', include('base.api.urls')),
     
     path('', views.routes),
     path('posts/', views.posts),
     path('post/<int:id>', views.post)
     
]

    