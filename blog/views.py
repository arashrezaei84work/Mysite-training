from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.template import loader
# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts' : posts
    }
    return render(request, "blog/blog-home.html", context)


def blog_detail(request, pid):
    posts = list(Post.objects.filter(status=1).order_by('id'))
    post = get_object_or_404(Post, pk=pid)
    post.counted_views += 1
    post.save()
    current_index = posts.index(post)
    perv_post = posts[current_index - 1] if current_index > 0 else  None
    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None

    context = {
        'post' :  post,
        'perv_post' : perv_post,
        'next_post' : next_post
    }
    return render (request, "blog/blog-single.html", context)

def test(request):
    # post = Post.objects.get(id=id)
    # post = get_object_or_404(Post, pk=id)
    # post = Post.objects.all().values()
    # temp = loader.get_template("test.html")
    # context = {
    #     'post' :  post
    # }
    return render(request, "test.html") 
    # return HttpResponse(temp.render(context, request))