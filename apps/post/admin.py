from django.contrib import admin
from apps.post.models import Post, PostComments

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComments)
