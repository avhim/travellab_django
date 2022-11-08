from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog-list.html'
    paginate_by = 10
    queryset = Post.objects.filter(active=True)


class BlogDetailView(DetailView):
    model = Post