from django.urls import path, include
from . import views as blog_view
from django.contrib.auth import views as auth_views


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
    path('search-blogs/', blog_view.SearchBlog.as_view(), name='search_blogs'),

    # password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
