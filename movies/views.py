from rest_framework import generics, views, response, status
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


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Movie.objects.all()

    def get(self, request):
        # Buscar todos os dados
        # Montar resposta
        # Devolve resposta pro user com estatíticas
        return response.Response(
            data={'messege': 'Funcionou'},
            status=status.HTTP_200_OK,
        )