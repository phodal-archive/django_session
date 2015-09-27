from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'session.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', 'blog.views.blog_lists', name='blog_lists'),

    url(r'^admin/', include(admin.site.urls)),
]
