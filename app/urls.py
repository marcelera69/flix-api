from django.contrib import admin
from django.urls import path, include
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

     path('api/v1/', include('genres.urls')),
     path('api/v1/', include('actors.urls')),
     path('api/v1/', include('movies.urls')),
     


     path('reviews', ReviewCreateListView.as_view(), name='review-create-list'),
     path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
