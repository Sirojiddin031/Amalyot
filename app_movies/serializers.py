from rest_framework import serializers
from .models import Movie, Actor, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.phone')

    class Meta:
        model = Comment
        fields = '__all__'
