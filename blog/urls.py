from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<str:category>/', views.category, name='category'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]