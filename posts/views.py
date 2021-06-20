from django.shortcuts import render, redirect

from main.models import RegisteredUser
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView


# show only current user posts
def my_posts(request):
    posts = Article.objects.order_by('-date')
    return render(request, 'posts/myposts.html', {'posts': posts})


# show all user posts
def all_posts(request):
    posts = Article.objects.order_by('-date')
    return render(request, 'posts/all-posts.html', {'posts': posts})


def tracking_posts(request):
    posts = Article.objects.order_by('-date')
    get_user = RegisteredUser.objects.all()
    try:
        first_user = get_user.first().user_id
        last_user = get_user.last().user_id
    except AttributeError:
        first_user = None
        last_user = None
    data = {
        'posts': posts,
        'first_user': first_user,
        'last_user': last_user
    }
    return render(request, 'posts/tracking-posts.html', data)


# Post details
class PostDetailView(DetailView):
    model = Article
    template_name = 'posts/post-details.html'
    context_object_name = 'article'


# update Post
class PostUpdateView(UpdateView):
    model = Article
    template_name = 'posts/update-post.html'
    form_class = ArticleForm


# delete Post
class PostDeleteView(DeleteView):
    model = Article
    success_url = '/posts/'
    template_name = 'posts/post-delete.html'


# create Post
class PostCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'posts/post-create.html'


# to get all regist users
# track = RegisteredUser.objects.all()

# to get first user
# print(track.first())

