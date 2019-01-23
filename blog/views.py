from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post,PostImage
from .forms import CommentForm


# Create your views here.
class PostLV(ListView):
    model = Post
    # 어떤 데이터를 꺼내쓸래??
    context_object_name = 'post_list'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    property = Post.objects.get(pk=1)
    image_list = property.images.all()
    comment_form = CommentForm()

    context = {
        'post' : post,
        'image_list' : image_list,
        'comment_form' : comment_form,
    }

    return render(request, 'blog/post_detail.html', context)
