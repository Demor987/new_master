from django.shortcuts import render
from blog.models import Post
from django.http import Http404

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'post': posts})

def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No post found.')
    return render(request, 'blog/post/detail.html', {'post': post})