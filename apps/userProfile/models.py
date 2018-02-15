from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


# Create your models here.

class UserModel(User):
    username_validator = UnicodeUsernameValidator()
    # username = models.CharField(
    #     'username',
    #     max_length=150,
    #     unique=True,
    #     help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_/ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': ("A user with that username already exists."),
    #         },
    # )
    # email = models.EmailField( max_length=150, blank=True)
    user_image = models.ImageField(
        upload_to='static/images',
        help_text="Profile Picture",
        blank=True, )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
