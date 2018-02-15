from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404
from django.urls import reverse
from django.views import View

from apps.post.forms import PostAddForm
from apps.post.models import Post, PostComments
from apps.userProfile.models import UserModel


# Create your views here.
def hello(rqequest):
    return render_to_response('response.html', {'variable': 'world'})


def home(request):
    # print('kkkkkkkkkkkkkkkkkkkkkkkkk', request.user_id)
    # print('kkkkkkkkkkkk', user)

    if authenticate != False:
        return HttpResponseRedirect(reverse('posts', args=[request.user.id]))
    else:
        return render(request, 'home.html', locals())


@login_required(login_url='/login')
def posts(request, user_id,):
    # form1=PostAddForm( request.POST or None)
    user = get_object_or_404(Post, id=3, )
    form1 = PostAddForm(request.POST, initial={
        'user': user
    })
    if request.POST and form1.is_valid():
        author = request.POST['author']
        post = form1.save(commit=False)
        post.author_id = author
        post.save()
        print('kkkkkkkkkkkk', user_id)
    # post = Post.objects.filter(id=user_id)
    post = Post.objects.all()
    # vv = get_object_or_404(Post, author=author)
    # print('pppppppppppp', vv)
    comment = PostComments.objects.filter(author_comment_id=Post('author_id'))

    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', comment)
    comentlist = [comment]
    for comentslenght in comentlist:
        try:
            comentCount = len(comentslenght)
            if comentCount < 1:
                return 0
        except:
            comentCount = 0

    context = {'comments': comment, 'posts': post, "comentCount": comentCount, 'form1': form1, 'user': user}
    return render(request, 'posts.html', context)


def detail(request, author_comment_id):
    return HttpResponse("You're looking at question %s." % author_comment_id)


class AddPost(View):
    def get(self, request, user_id):
        user = get_object_or_404(Post, id=user_id)
        form = PostAddForm(initial={
            'user': user
        })
        print('krakadil')
        return render(request, 'posts.html', {'user': user, 'form': form}, locals())
        # return render(request, 'posts.html', locals())

    def post(self, request, user_id):
        if request.POST:
            form = PostAddForm(request.POST or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                print(form)
                return render(request, 'posts.html', {'user': user, 'form': form}, locals())
            else:
                form = PostAddForm()
            return render(request, 'posts.html', {'user': user, 'form': form}, locals())


def chek_username(request):
    if request.GET:
        user_name = request.GET['username']
        users = UserModel.objects.values('username')
        listt = []
        for usernames in users:
            listt.append(usernames.values())
            print(listt)
            x = listt
        if user_name in str(x):
            print('mtav arajin@')
            return HttpResponse('no', content_type='text/html')
        else:
            print('mtav erkrord@')
            print(listt)
            print(user_name)
            return HttpResponse('ok', content_type='text/html')
    else:
        print('mtav verj@')
        return HttpResponse('ok', content_type='text/html')


def check_email(request):
    if request.GET:
        email = request.GET['email']
        users_email = UserModel.objects.values('email')
        listt = []
        print('request email', email)
        for emaill_user in users_email:
            listt.append(emaill_user.values())
            x = listt
        if str(email) in str(x):
            return HttpResponse('no', content_type='text/html')
        else:
            print('mtav erkrord@')
            return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('ok', content_type='text/html')
