from django.shortcuts import render, redirect
from .models import Post #import the Post
from django.contrib.auth.decorators import login_required # decorator on function,
from . import forms
# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date') # get all of the object for us, order by descending way minus sign
    return render(request, 'posts/posts_list.html', {'posts': posts}) #add posts in dictionary, passing data on the template

def post_page(request, slug): # create function for post page
    post = Post.objects.get(slug=slug) # pass to get one post we have that matches slug
    return render(request, 'posts/post_page.html', {'post': post}) #add posts in dictionary, passing data on the template

@login_required(login_url="/users/login") #checks when function runs to see if user login
def post_new(request):
    if request.method == 'POST': # should be POST request
        form = forms.CreatePost(request.POST, request.FILES) #sending also an image file
        if form.is_valid(): # validate what submitted against the model
            # save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else: # else is the GET request
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })