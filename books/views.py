from django.shortcuts import render
from .models import Book,Review,Userprofile
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,status,permissions
from .serializers import BookSerializer,ReviewSerializer,UserProfileSerializer
from django.db.models import Avg
from rest_framework.response import Response


# Create your views here.
''' List, Create  Books for a given request '''
class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        book_id=self.kwargs['pk']
        return Review.objects.filter(book_id=book_id)
    
    def perform_create(self, serializer):
        book=Book.objects.get(pk=self.kwargs['pk'])
        user=self.request.user
        serializer.save(book=book,user=user)

@api_view(["GET"])
def book_summary(request,pk):
    try:
        books=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    reviews=Review.objects.filter(book=books)
    avg_rating=reviews.aggregate(Avg('rating'))['rating__avg']
    return Response({'summary':books.summary,'average_rating':avg_rating})

class GenerateSummaryView(APIView):
    def post(self,request):
        #content=request.data['content']
        summary="personal finance book of all time."#should be replaced with AI Summary
        return Response({'summary':summary})
    
    
class RecommendationsViews(APIView):
    def get(self,request):
        try:
            user_profile=Userprofile.objects.get(user=request.user)
        except Userprofile.DoesNotExist:
            return Response({"user not found",user_profile})
        preferred_genres=user_profile.preferred_genres
       
        preferred_authors=user_profile.preferred_authors
        books=Book.objects.filter(
            genre__in=preferred_genres.split(','),
            author__in=preferred_authors.split(',')
        )
       
        serilazer=BookSerializer(books,many=True)
        return Response(serilazer.data)
    
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_object(self):
        return self.request.user.userprofile
    


