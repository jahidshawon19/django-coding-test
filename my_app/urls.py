from my_app import views
from django.urls import path

urlpatterns = [
  path('', views.index, name='home'),
  

  path('add_image/', views.addImage, name='add-image'),
  path('add_product/', views.addProduct, name='add-product'),
]


