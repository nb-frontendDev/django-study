from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('タイトル',max_length=200)
    content = models.TextField('本文')
    created = models.DateTimeField('作成日', default=timezone.now)

    # __str__関数
    def __str__(self):
        return self.title