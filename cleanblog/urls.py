"""cleanblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import xadmin
from django.conf.urls import url, include
from cleanblog.settings import MEDIA_ROOT
from django.views.static import serve
from blog.feed import AllPostRssFeed

xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

from ckeditor_uploader import urls as ckeditor_uploader_urls

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^ckeditor/', include(ckeditor_uploader_urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^all/rss/$', AllPostRssFeed(), name='rss'),
]
