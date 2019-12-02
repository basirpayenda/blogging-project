from django.urls import path, include
from . import views as blog_view


urlpatterns = [
    path('', blog_view.PostListView.as_view(), name='blog-home'),
    path('posts/<str:username>/',
         blog_view.UserPostsView.as_view(), name='users-posts'),

    path('new_post/', blog_view.PostCreateView.as_view(), name='blog-create'),

    path('post/<slug:title_slug>/update/',
         blog_view.PostUpdateView.as_view(), name='blog-update'),

    path('post/<slug:title_slug>/delete/',
         blog_view.PostDeleteView.as_view(), name='blog-delete'),

    path('post/<slug:title_slug>/', blog_view.post_detail, name='blog-detail'),
    path('about/', blog_view.about, name='blog-about'),
    path('tinymce/', include('tinymce.urls')),

]
