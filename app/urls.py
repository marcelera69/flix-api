from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListVIew, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListVIew.as_view() , name='genre-create-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view')
]
