from django.urls import path
from .views import BookmarkCreateView, BookmarkListView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name = 'bookmark_list'),
    path('add/', BookmarkCreateView.as_view(), name = 'bookmark_create'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='bookmark_detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name = 'bookmark_update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name = 'bookmark_delete'),
]