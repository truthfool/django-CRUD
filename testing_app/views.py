from django.shortcuts import render
from .forms import UserForm
from .models import UserModel
from django.http import HttpResponseRedirect
# Create your views here.


def create_user(request):
    # Code executed when request is post otherwise display empty form from below context
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context = {
        'form': form
    }
    return render(request, 'create_user.html', context)


def post_details(request):
    posts = UserModel.objects.all()

    context = {
        'post_value': posts
    }

    return render(request, 'post_details.html', context)


def user_details(request, id):
    post = UserModel.objects.get(id=id)

    context = {
        'user_details': post
    }

    return render(request, 'user_details.html', context)


def update_user(request, id):
    post = UserModel.objects.get(id=id)

    form = UserForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context = {
        'form': form
    }

    return render(request, 'update_user.html', context)


def delete_user(request, id):
    post = UserModel.objects.get(id=id)

    post.delete()
    return HttpResponseRedirect('/')
