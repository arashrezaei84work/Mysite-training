from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name="totalpost")
def myfunc():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name="posts")
def myfunc():
    post = Post.objects.filter(status=1)
    return post

@register.filter
def snippts(value, arg=25):
    return value[:arg] + "..."

@register.inclusion_tag("blog/blog-popular-post.html")
def latestpost():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {"posts" : posts}