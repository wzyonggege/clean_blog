from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from comments.forms import CommentForm

def index(request):
    post_list = Post.objects.all() #.order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    comment_list = post.comment_set.all()
    return render(request, 'post.html', context={'post': post,
                                                 'form': form,
                                                 'comment_list': comment_list})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list  = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})