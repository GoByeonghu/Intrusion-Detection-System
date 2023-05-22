from . import views
from django.urls import path
import include

urlpatterns = [
    path('', views.post_list, name='post_list'),
]