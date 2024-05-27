from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from app.permissions import GlobalPermissions



class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer