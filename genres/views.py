from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalPermissions



class GenreCreateListVIew(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

