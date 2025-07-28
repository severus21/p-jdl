"""jdl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import re_path, include


from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

from jdl_web.sitemap import StaticViewSitemap as JDLWebStaticViewSitemap
sitemaps = {
    'static.jdl_web': JDLWebStaticViewSitemap,
}

urlpatterns = [
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'', include('jdl_web.urls', namespace="jdl_web")),
]

if settings.DEBUG :
    from django.conf.urls.static import static
    urlpatterns.extend( static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) ) 
    urlpatterns.extend( static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) )

