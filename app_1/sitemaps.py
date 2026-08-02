from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['app_1:index', 'app_1:about', 'app_1:contact']

    def location(self, item):
        return reverse(item)
