from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)    # first option
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ()   :  you can access to edit only this fields
    list_display = ('id','title', 'author' ,'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    # ordering = ['created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Category)
# admin.site.register(Post, PostAdmin)      <==  another option : second option
