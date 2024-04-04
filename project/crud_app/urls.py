from django.urls import path
from .views import *
urlpatterns = [
     path('add/',Add_View.as_view(), name='add_url'),
     path('show/',Show_View.as_view(), name='show_url'),
     path('update/<int:pk>/',Update_View.as_view(), name='update_url'),
     path('delete/<int:pk>/',Delete_View.as_view(), name='delete_url')
 ]