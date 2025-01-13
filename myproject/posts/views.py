from django.shortcuts import render
from .models import Post #import the Post

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date') # get all of the object for us, order by descending way minus sign
    return render(request, 'posts/posts_list.html', {'posts': posts}) #add posts in dictionary, passing data on the template

# create function for post page
def post_page(request, slug):
    post = Post.objects.get(slug=slug) # pass to get one post we have that matches slug
    return render(request, 'posts/post_page.html', {'post': post}) #add posts in dictionary, passing data on the template