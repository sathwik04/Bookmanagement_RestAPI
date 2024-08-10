from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Review, Userprofile
from rest_framework_simplejwt.tokens import RefreshToken
 
class APITestSetup(APITestCase):
 
    def setUp(self):
        self.user = User.objects.create_user(username='phani_user', password='rootroots')
        self.user_profile = Userprofile.objects.create(user=self.user, preferred_genres='Finance', preferred_authors='Robart')
        self.book = Book.objects.create(title='Rich Dad Poor Dad', author='Robart', genre='Finance',  summary='Test Summary')
        self.book2 = Book.objects.create(title='Another Book', author='Colan', genre='Finance',  summary='AnotherSummary')
        self.review = Review.objects.create(book=self.book, user_id=self.user.id, review_text='Great book!', rating=5)
 
        self.token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
 
    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)
 
class BookTests(APITestSetup):
 
    def test_create_book(self):
        url = reverse('book-list-create')
        data = {
            "title": "New Book",
            "author": "New Author",
            "genre": "Fantasy",
        
            "summary": "New Summary"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
 
    def test_get_books(self):
        url = reverse('book-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
 
    def test_get_book_detail(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Rich Dad Poor Dad')
 
    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "genre": "Finance",
            
            "summary": "Updated Summary"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
 
    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
 
class ReviewTests(APITestSetup):
 
    def test_create_review(self):
        url = reverse('review-list-create', args=[self.book.id])
        
        data = {
            "user_id": self.user.id,
            "review_text": "Another great book!",
            "rating": 4,
            "book":self.book.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)
 
    def test_get_reviews(self):
        url = reverse('review-list-create', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
 
class UserprofileTests(APITestSetup):
 
    def test_get_user_profile(self):
        url = reverse('user-profile')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['preferred_genres'], 'Finance')
        self.assertEqual(response.data['preferred_authors'] , 'Robart')

class RecommendationTests(APITestSetup):
 
    def test_get_recommendations(self):
        url = reverse('book-recommendations')
        userprofile=Userprofile.objects.get(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
 
class SummaryTests(APITestSetup):
 
    def test_generate_summary(self):
        url = reverse('generate-summary')
        data = {
            "content": "This is the content of the book."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('summary', response.data)
