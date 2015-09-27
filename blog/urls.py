from django.conf.urls import include, url
from blog.views import blog_lists

urlpatterns = [
    url(r'^', blog_lists),
]
