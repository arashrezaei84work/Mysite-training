from django.contrib import admin
from app_1.models import Contact, NewsLetter


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','subject' ,'email' ,'created_date')
    list_filter = ('email',)
    search_fields = ['subject', 'message']

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('email',)
