from django.urls import path
##from . import views
from .views import home_view, mision_view, loginPage, logoutPage, perfilPage, registro, post


urlpatterns = [
    path('', home_view),
    path('login/', loginPage),
    path('logout/', logoutPage),
    path('perfil/', perfilPage),
    path('mision/', mision_view),
    path('mision/<int:id>', mision_view),
    path('registro/', registro),
    path('post/', post)
]