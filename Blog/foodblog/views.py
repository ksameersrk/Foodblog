from django.shortcuts import render, redirect
from .forms import *

#Model and templates connected via Views
from .models import *

# Create your views here.
def post_list(request):
    posts = Post.objects.all()#filter(published_date__lte=timezone.now()
    #order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            posts = Post.objects.all()
            auth = form.save(commit=False)
            auth.save()
            return render(request, 'blog/post_list.html', {'name':auth.username,
                'posts':posts})
    else:
        form = AuthForm()
    return render(request, 'blog/signup.html', {'form': form})

def post_old(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            auth = Auth.objects.all()
            posts = Post.objects.all()
            login = form.save(commit=False)
            for user_details in auth:
                if user_details.username == login.username and user_details.password == login.password:
                 return render(request, 'blog/post_list.html', {'name':login.username,
                'posts':posts})
            return render(request, 'blog/login.html', {'form': form,'name':login.username})
    else:
        form = Login()
    return render(request, 'blog/login.html', {'form': form})

def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            allposts = Post.objects.all()
            return render(request, 'blog/post_list.html', {'name':post.author,
                'posts':allposts})
    else:
        form = PostForm()
    return render(request, 'blog/writepost.html', {'form': form})