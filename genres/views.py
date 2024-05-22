from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer



class GenreCreateListVIew(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

