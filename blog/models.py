from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    image = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to='blogimage/%Y/%m/%d',
            format='JPEG',
            options={'quality': 80})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name #태그의 이름이 표시


class Notice(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            format='JPEG',
            options={'quality': 80})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    # 이 코멘트는 Post 모델에 대해서 1:N의 관계를 가진다
    # post_id 라는 필드가 생김 외래키의 영향
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
