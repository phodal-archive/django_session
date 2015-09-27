from django.shortcuts import render
from blog import models


def blog_lists(request):
    """A view of all bands."""
    blogs = models.Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})
