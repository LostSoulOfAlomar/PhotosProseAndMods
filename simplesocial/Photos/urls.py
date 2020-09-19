from django.urls import path
from . import views

app_name = 'Photos'

urlpatterns = [
    path('photoshome', views.PhotosHome.as_view(), name="photoshome"),

]
