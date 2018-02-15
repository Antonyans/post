# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from apps.userProfile.models import UserModel


# from apps.register.models import User

class UserUpdateForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ( 'email', 'user_image')
