from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import BlogPost


def main_view(request):
    blogs = BlogPost.objects.order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'index.html', context=context)


def login_frontend(request):
    return render(request, 'login.html')


def login_backend(request):
    username = request.POST['login']
    password = request.POST['passw1']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/login')


def logout_backend(request):
    logout(request)
    return redirect('/login')


def register_frontend(request):
    return render(request, 'register.html')


def register_backend(request):
    username = request.POST['login']
    email = request.POST['email']
    password = request.POST['passw1']
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('/')
    except:
        return redirect('/register')


def add_frontend(request):
    if request.user.is_authenticated:
        return render(request, 'add_post.html')
    return redirect('/login')


def add_backend(request):
    title = request.POST['title']
    text = request.POST['text']
    if request.user.is_authenticated:
        author = request.user.username
        blog_post = BlogPost(title=title, text=text, author=author)
        blog_post.save()
        return redirect('/')

    return redirect('/login')


def view(request):
    try:
        _id = int(request.GET['id'])
        blog = BlogPost.objects.get(id=_id)
        context = {
            'blog': blog
        }
        return render(request, 'view.html', context=context)
    except:
        return redirect('/')
