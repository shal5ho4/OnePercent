from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import resolve_url


class StaticSiteMap(Sitemap):
    changefreq = 'never'
    priority = 0.8

    def items(self):
        return ['home:home', 'query:create']
    
    def location(self, obj):
        return resolve_url(obj)


sitemaps = {'static': StaticSiteMap}


urlpatterns = [
    path('onepercentadmin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('form/', include('query.urls', namespace='query')),
    path('sitemap.xml/', sitemap, 
        {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
