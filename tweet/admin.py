from django.contrib import admin
from .models import Tweet

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['user','text','photo']