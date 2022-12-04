from django.contrib import admin
from .models import Post

# registerでPostを登録する
admin.site.register(Post)