from django.urls import path
from . import views

urlpatterns = [
    path('hello.html', views.home, name='home'),  # Add this line
    #path('index/', views.index, name='index'),  # Assuming you have an index view
]
