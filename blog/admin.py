from django.contrib import admin
from .models import Blog, Comment, Hashtag, Bookmark

# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Hashtag)
admin.site.register(Bookmark)