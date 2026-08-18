from django import template
from django.shortcuts import get_object_or_404
from blog.models import Post, Category, Comment
register = template.Library()

@register.simple_tag(name="totalpost")
def myfunc():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name="posts")
def myfunc():
    post = Post.objects.filter(status=1)
    return post

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=1).count()


@register.filter
def snippts(value, arg=25):
    return value[:arg] + "..."

@register.inclusion_tag("blog/blog-popular-post.html")
def latestpost(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {"posts" : posts}

@register.inclusion_tag("blog/blog-category.html")
def postcategories():
    post = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = post.filter(category=name).count
    return {'categories' : cat_dict}

@register.inclusion_tag('app_1/recent-blog-post.html')
def recentPost(arg=6):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts' : posts }

@register.inclusion_tag("blog/next&perv.html")
def next_perv(post):
    posts = list(Post.objects.filter(status=1).order_by('id'))

    current_index = posts.index(post)
    perv_post = posts[current_index - 1] if current_index > 0 else  None
    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None
    return  {'perv_post' : perv_post, 'next_post' : next_post}
  



