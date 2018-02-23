from apps.userProfile.models import UserModel
from django.contrib.auth.forms import UserCreationForm


# from apps.register.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2', 'user_image')
