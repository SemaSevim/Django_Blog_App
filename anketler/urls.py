from importlib.resources import path
from django.urls import path
from . import views 


app_name = 'anketler'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.AyrintiView.as_view(), name='ayrinti'),
    path('<int:pk>/sonuclar/', views.SonuclarView.as_view(), name='sonuclar'),
    path('<int:soru_id>/oy/', views.oy, name='oy'),
]