from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


# Create your views here.
class PostLV(ListView):
    model = Post
    # 어떤 데이터를 꺼내쓸래??
    context_object_name = 'post_list'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html',{'post':post})
