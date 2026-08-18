from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Comment
from django.template import loader
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat') != None:
        posts = posts.filter(category__name=kwargs['cat'])
    if kwargs.get('author_name') != None:
        posts = posts.filter(author__username=kwargs['author_name'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
        
   
    posts = Paginator(posts, 1)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {
        'posts' : posts
    }
    return render(request, "blog/blog-home.html", context)

def blog_detail(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited.')
        else:
            messages.add_message(request,messages.ERROR,'your comment did not submited!')
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_views += 1
    post.save(update_fields=['counted_views'])
    if  post.login_require and not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))
    
    comments = Comment.objects.filter(post=post.id,approved=1)
    form = CommentForm()
    context = {
        'post' :  post,
        'form' : form,
        'comments' : comments,
    }
    return render (request, "blog/blog-single.html", context)

    

    

def blog_category(request,cat):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat)
    context = {
        'posts' : posts,
    }
    return render(request, "blog/blog-home.html", context)



def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):    
            posts = posts.filter(content__contains=s)
    context = {
        'posts' : posts
    }
    return render(request, "blog/blog-home.html", context)


# def test(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('OK')
#         else:
#             return HttpResponse('failed')

#     form = ContactForm()
#     return render(request, "test.html",{'form' : form}) 
