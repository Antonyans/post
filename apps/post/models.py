from django.db import models

from apps.userProfile.models import UserModel


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    def __str__(self):
        return str(self.id)
        print ('iiiiiiiiiiiiiiiiii',str(self.id))


class PostComments(models.Model):
    author_comment = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post_coment = models.ForeignKey(Post, on_delete=models.CASCADE)
    text_coment = models.TextField(max_length=300)
    create_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_comment.username


class Likes(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def __str__(self):
        return str(self.likes)
