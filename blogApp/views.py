from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import F
from .forms import PostForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blogApp/home.html'
    ordering = '-created_at'
    paginate_by = 3


def post_detail(request, title_slug):
    obj = get_object_or_404(Post, slug=title_slug)
    session_key = f'user_{title_slug}'

    if not request.session.get(session_key, False):
        type(obj).objects.filter(pk=obj.pk).update(
            view_counts=F('view_counts') + 1
        )
        request.session[session_key] = True

    return render(request, 'blogApp/detail.html', {'post': obj})


""" class PostDetailView(DetailView):
    model = Post
    template_name = 'blogApp/detail.html' """


class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    form_class = PostForm
    template_name = 'blogApp/update.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

    def get_object(self):
        slug = self.kwargs.get('title_slug')
        return get_object_or_404(Post, slug=slug)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blogApp/delete.html'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

    def get_object(self):
        slug = self.kwargs.get('title_slug')
        return get_object_or_404(Post, slug=slug)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogApp/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostsView(ListView):
    # model = Post
    queryset = Post.objects.all()
    template_name = 'blogApp/users_posts.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=get_object_or_404(User, username=self.kwargs.get('username'))).order_by('-date_created')


@login_required
def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'blogApp/about.html', context)
