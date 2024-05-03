from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
     path('reviews', views.ReviewCreateListView.as_view(), name='review-create-list'),
     path('reviews/<int:pk>', views.ReviewRetrieveUpdateDestroyView.as_view(), 
          name='review-detail-view'),
]
