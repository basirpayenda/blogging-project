from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(
        default='default.jpg', upload_to='posts/%Y/%m/%d')
    view_counts = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'title_slug': self.slug})

    def get_update_url(self):
        return reverse('blog-update', kwargs={'title_slug': self.slug})

    def get_delete_url(self):
        return reverse('blog-delete', kwargs={'title_slug': self.slug})


""" def save(self, *args, **kwargs):
        img = Image.open(self.thumbnail.path) """
