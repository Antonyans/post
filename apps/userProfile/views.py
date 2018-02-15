from django.shortcuts import render
from django.views.generic.edit import UpdateView
from apps.userProfile.forms import UserUpdateForm


# Create your views here.
class UserUpdateView(UpdateView):

    def get(self, request):
        form = UserUpdateForm()
        return render(request, 'registration/myAccount.html', locals())


    def post(self, request):
        form = UserUpdateForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            message = ('lriv ok')
            return render(request, 'registration/myAccount.html', {'message': message})
            
