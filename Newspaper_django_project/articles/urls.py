from django.urls import path
from .views import (
    ArticleListView, 
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentPost)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/comment', CommentPost.as_view(), name='comment_post'),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]