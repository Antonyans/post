from apps.userProfile.models import UserModel
from django.contrib.auth.forms import UserCreationForm


# from apps.register.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2', 'user_image')

        # def save(self, commit=True):
        #     user = super(UserForm, self).save(commit=False)
        #     user.username = self.cleaned_data['username']
        #     user.email = self.cleaned_data['email']
        #     user.password1 = self.cleaned_data['password1']
        #     user.password2 = self.cleaned_data['password2']
        #     user.user_image = self.cleaned_data['user_image']
        #
        #     if commit:
        #         user.save()
        #     return user
