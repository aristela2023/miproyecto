from django.urls import path
##from . import views
from .views import home_view, mision_view, perfil, registro, post


urlpatterns = [
    path('', home_view),
    path('mision/', mision_view),
    path('mision/<int:id>', mision_view),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro),
    path('post/', post)
]