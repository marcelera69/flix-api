from django.contrib import admin
from django.urls import path, include
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroy
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

     path('api/v1/', include('genres.urls')),
     path('api/v1/', include('actors.urls')),
     


     path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
     path('movies/<int:pk>', MovieRetrieveUpdateDestroy.as_view(), name='movie-detail-view'),


     path('reviews', ReviewCreateListView.as_view(), name='review-create-list'),
     path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
