from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            comment = Comment(name=name, email=email, content=content)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            return render(request, 'post.html', context={'post': post,
                                                         'form': form,
                                                         'comment_list':comment_list})

    return redirect(post)