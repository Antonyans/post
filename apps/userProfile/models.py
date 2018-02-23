from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


# Create your models here.

class UserModel(User):
    username_validator = UnicodeUsernameValidator()
    user_image = models.ImageField(
        upload_to='static/images',
        help_text="Profile Picture",
        blank=True, )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
