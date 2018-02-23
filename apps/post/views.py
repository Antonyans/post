import json

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from apps.post.forms import PostAddForm, CommentFormAdd
from apps.post.models import Post, PostComments, Likes
from apps.userProfile.models import UserModel


# Create your views here.
def hello(rqequest):
    return render_to_response('response.html', {'variable': 'world'})


def home(request):
    # print('kkkkkkkkkkkk', user)

    if authenticate != False:
        print('kkkkkkkkkkkkkkkkkkkkkkkkk', request.user.id)

        # return HttpResponseRedirect(reverse('posts', args=[request.user.id]))
        return redirect('signin')
    else:
        return render(request, 'home.html', locals())


@login_required(login_url='/login')
def posts(request,):
    form1 = PostAddForm(request.POST)
    if request.POST and form1.is_valid():
        # author = request.POST['author']
        post = form1.save(commit=False)
        post.author_id = request.user.id
        post.save()
    postlist = Post.objects.all().order_by('-create_data')
    paginator = Paginator(postlist, 5)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    context = {'posts': post, 'form1': form1, }
    return render(request, 'posts.html', context)


def comments(request, post_id=1):
    form = CommentFormAdd(request.POST)
    if request.POST and form.is_valid():
        author_comment = request.POST['author_comment']
        post_coment = request.POST['post_coment']
        comment = form.save(commit=False)
        comment.post_coment_id = int(post_coment)
        comment.author_comment_id = author_comment
        comment.save()
    else:
        form = CommentFormAdd()
    try:
        post = Post.objects.get(id=post_id)
    except AttributeError:
        return HttpResponse('no posts')
    try:
        comment = PostComments.objects.filter(post_coment_id=post_id)
    except AttributeError:
        return HttpResponse('no posts')
    comentlist = [comment]
    for comentslenght in comentlist:
        try:
            comentCount = len(comentslenght)
            if comentCount < 1:
                comentCount = 0
        except:
            comentCount = 0
    context = {'post': post, 'comments': comment, 'comentCount': comentCount, 'form': form,}
    return render(request, 'postcoments.html', context)


def search(request):
    querry = request.GET.get('q')
    print(querry)
    search_list = list(Post.objects.filter(
        Q(text__icontains=querry)
        # Q(author__icontains=querry)
    ).order_by('-create_data'))
    # paginator = Paginator(search, 2)
    # page = request.GET.get('page')
    # search_list = paginator.get_page(page)
    return_str = render_to_string('ajaxsearch.html', {'search_list': search_list, 'q':querry,})
    return HttpResponse(json.dumps(return_str), content_type='application/json')
    # return render_to_response('home.html', {'search_list': search_list})

def addlike(request, post_id):
# def addlike(request):
    user =  request.user.id
    post = post_id
    nolike = Likes.objects.filter(author_id=user, post_id=int(post))
    if nolike:
        print('layq@ arden ka')
        like =Likes.objects.get(author_id=user, post_id=int(post))
        like.delete()
        postLike = Post.objects.get(id=int(post))
        postLike.like -= 1
        postLike.save()
        return HttpResponse('dislike')

    else:
        print('avelacnel like')
        like =Likes.objects.create(author_id=user, post_id=int(post))
        postLike = Post.objects.get(id=int(post))
        postLike.like += 1
        postLike.save()
        like.likes  +=1
        like.save()
        return HttpResponse('like')
    # return render(request, 'posts.html')
    return HttpResponse('like')



def likecount(request):
    likelist = Likes.objects.filter(post_id=int(post))
    likes = [likelist]
    for likelenght in likes:
        try:
            likecount = len(likelenght)
            if likecount < 1:
                likecount = 0
        except:
            likecount = 0
    context = {'likecount':likecount}
    return render(request, 'posts.html', context)


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
        users = UserModel.objects.filter(username=user_name)
        if users:
            return HttpResponse('no', content_type='text/html')
        else:
            return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('ok', content_type='text/html')


def check_email(request):
    if request.GET:
        email = request.GET['email']
        users_email = UserModel.objects.filter(email=email)
        if users_email:
            return HttpResponse('no', content_type='text/html')
        else:
            return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('ok', content_type='text/html')
