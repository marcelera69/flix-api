from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListVIew, GenreRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListVIew.as_view() , name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view() , name='genre-detail-view')
]
