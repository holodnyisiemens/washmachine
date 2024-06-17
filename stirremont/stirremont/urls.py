from django.contrib import admin
from django.urls import path, include, re_path
from services.views import page_not_found
from django.views.generic import TemplateView
from .sitemaps import ServiceSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    '': ServiceSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='stirremont/robots.txt', content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = page_not_found
