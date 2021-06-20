from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_posts, name='my_posts'),
    path('all-posts', views.all_posts, name='all_posts'),
    path('tracking-posts', views.tracking_posts, name='tracking_posts'),
    path('create', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]