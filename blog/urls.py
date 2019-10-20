from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
	path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail' ),
	path('post/<uuid:pk>/update/', PostUpdateView.as_view(), name='post-update' ),
	path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name='post-delete' ),
	path('post/new/', views.PostCreateView, name='post-create'),
	path('about/', views.about, name='blog-about'),
]