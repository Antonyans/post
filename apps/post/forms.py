from django.forms import ModelForm

from apps.post.models import Post, PostComments


class PostAddForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']

class CommentFormAdd(ModelForm):
    class Meta:
        model = PostComments
        fields = ['text_coment',]
