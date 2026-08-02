from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ('published_date',)
        # verbose_name = ????
        #verbose_name_plural = ????
    def __str__(self):
        return f" {self.title} - {self.id}"
    
    # def snipts(self):
    #     return self.content[:150] + ' . . .'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pid':self.id})
        