from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('genres/', views.GenreCreateListVIew.as_view() , name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetriveUpdateDestroyView.as_view() , 
         name='genre-detail-view'),
]