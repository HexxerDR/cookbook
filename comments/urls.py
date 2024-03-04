from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comments-create'),
    path('recipe/<int:post_pk>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comments-delete'),
    path('recipe/<int:post_pk>/comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comments-update'),
]

    