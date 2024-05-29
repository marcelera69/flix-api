from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from app.permissions import GlobalPermissions
from reviews.models import Review


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
        total_movies = self.queryset.count()
        movies_by_genere = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genere': movies_by_genere,
                'totalt_reviews': total_reviews,
                'average_stars': round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
    
