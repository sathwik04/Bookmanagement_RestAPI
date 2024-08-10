from rest_framework import serializers
from .models import Book, Review,Userprofile

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['book','user','review_text','rating']
        read_only_fields=['book','user']
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userprofile
        fields=['preferred_genres','preferred_authors']

    