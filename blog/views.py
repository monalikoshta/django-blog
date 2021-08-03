from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html',{'posts': posts})

def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_blogs.html',{'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request,'blog/post_detail.html',{'post': post})

def bloggers(request):
    users = User.objects.all()
    print(users)
    return render(request, 'blog/bloggers.html',{'users': users})

# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/')
#     else:
#         return redirect('/')

def user_detail(request, username):
    user = User.objects.get(username=username)
    return render(request,'blog/user_detail.html',{'user': user})
