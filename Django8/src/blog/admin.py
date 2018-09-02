from django.contrib import admin
from .models import *
from pip._vendor.requests.api import post
# Register your models here.

admin.site.register(Post)
admin.site.register(PostType)
admin.site.register(Image)
admin.site.register(File)