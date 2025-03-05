from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from app_movies.models import Movie, Actor, Comment
from app_movies.permissions import IsAdminOrReadOnly, IsAdminOwnerOrReadOnly, IsOwnerOrReadOnly
from app_movies.serializers import MovieSerializer, ActorSerializer, CommentSerializer

from .models import Movie, Actor, Comment
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer



@method_decorator(csrf_exempt, name='dispatch')
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]  


class MovieList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOrReadOnly]
     queryset = Movie.objects.all()
     serializer_class = MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAdminOrReadOnly]

class ActorList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOrReadOnly]
     queryset = Actor.objects.all()
     serializer_class = ActorSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]  
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)  # Kommentni foydalanuvchiga bog‘lash


class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        return Comment.objects.filter(movie_id=movie_id)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOwnerOrReadOnly,IsAuthenticated]
     serializer_class = CommentSerializer

     def get_queryset(self):
         movie_id = self.kwargs.get('movie_id')
         comment_id = self.kwargs.get('pk')

         return Comment.objects.filter(id=comment_id,movie_id=movie_id)

