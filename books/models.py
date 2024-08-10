from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    summary=models.TextField()

    def __str__(self) -> str:
        return f' {self.title}'

class Review(models.Model):
    book=models.ForeignKey(Book,related_name='reviews',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    review_text=models.TextField()
    rating=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Review of {self.book.title}'
    
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    preferred_genres=models.TextField()
    preferred_authors=models.TextField()
    
    def __str__(self) -> str:
        return self.user.username
