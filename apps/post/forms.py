from django.forms import ModelForm

from apps.post.models import Post


class PostAddForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', ]
