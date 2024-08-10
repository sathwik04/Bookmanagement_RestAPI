from django.contrib import admin
from django.urls import path
from books import views,swagger
from .swagger import schema_view

urlpatterns=[
    path('api/books/',views.BookListCreateView.as_view(),name='book-list-create'),
    path('api/books/<int:pk>/',views.BookDetailView.as_view(),name='book-detail'),
    path('api/books/<int:pk>/reviews/',views.ReviewListCreateView.as_view(),name='review-list-create'),
    path('api/books/<int:pk>/summary/',views.book_summary,name='book-summary'),
    path('api/books/generate-summary/',views.GenerateSummaryView.as_view(),name='generate-summary'),
    path('api/recommendations/',views.RecommendationsViews.as_view(),name='book-recommendations'),
    path('api/userprofile/',views.UserProfileView.as_view(),name='user-profile'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

