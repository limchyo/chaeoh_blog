from django.contrib import admin
from .models import Article, Comment, Hashtag

# Register your models here.
@admin.register(Article, Comment, Hashtag)
class FeedAdmin(admin.ModelAdmin):
    pass
