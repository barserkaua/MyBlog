from django.shortcuts import render, redirect

from user.models import RegisteredUser
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def posts_home(request):
    posts = Article.objects.order_by('-date')
    return render(request, 'posts/myposts.html', {'posts': posts})


def all_posts(request):
    posts = Article.objects.order_by('-date')
    return render(request, 'posts/all-posts.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Article
    template_name = 'posts/post-details.html'
    context_object_name = 'article'


class PostUpdateView(UpdateView):
    model = Article
    template_name = 'posts/update-post.html'
    form_class = ArticleForm


class PostDeleteView(DeleteView):
    model = Article
    success_url = '/posts/'
    template_name = 'posts/post-delete.html'


def create(request):
    form = ArticleForm()

    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/post-create.html', data)
