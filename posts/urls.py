from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('all-posts', views.all_posts, name='all_posts'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]