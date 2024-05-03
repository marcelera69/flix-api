from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
     path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),
     path('movies/<int:pk>', views.MovieRetrieveUpdateDestroy.as_view(), 
          name='movie-detail-view'),
]