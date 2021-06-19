
from Blog_app.forms import CommForm, UserRegistation
from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blog, Comment, User
from django.db.models import Q, query
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout, login, user_login_failed

# Create your views here.


def home(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'blog_app/home.html', context)


def about(request):
    return render(request, 'blog_app/about.html', )


def single_post(request, slug):
    post = Blog.objects.get(slug=slug)
    comments = post.comment.all()
    latest_post = post.tag.similar_objects()[:3]

    if request.method == "POST":
        new_comm = CommForm(request.POST)
        if new_comm.is_valid():
            new_comm = new_comm.save(commit=False)
            new_comm.post = post
            new_comm.save()

            # messages.success(request, 'Comment Success')
            return HttpResponseRedirect(request.path_info)

    else:
        new_comm = CommForm()

    return render(request, 'blog_app/single_post.html', {'post': post, 'new_comm': new_comm, 'comments': comments, 'latest_post': latest_post})


def log_in(request):
    if request.method == 'POST':
        fm = UserRegistation(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            regist = User(name=name, email=email, password=password)
            regist.save()
            return redirect('/')
    else:
        fm = UserRegistation()

    return render(request, 'blog_app/login.html', context={'form': fm})


def log_out(request):
    logout(request)
    return redirect('/')


def user_delete(request, id):
    if request.method == 'POST':
        usr = User.objects.get(pk=id)
        usr.delete()
    return HttpResponseRedirect('/')
