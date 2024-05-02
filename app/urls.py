from django.contrib import admin
from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroy
from genres.views import GenreCreateListVIew, GenreRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

     path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
     path('movies/<int:pk>', MovieRetrieveUpdateDestroy.as_view(), name='movie-detail-view'),

    path('genres/', GenreCreateListVIew.as_view() , name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view() , 
         name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), 
         name='actor-detail-view' ),

     path('reviews', ReviewCreateListView.as_view(), name='review-create-list'),
     path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
