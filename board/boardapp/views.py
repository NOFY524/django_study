from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Post, Comment
from .forms import PostUploadForm, CommentUploadForm

# Create your views here.


def index(request):
    post_list = Post.objects.order_by('-create_time')
    post_dict = {'post_list': post_list}

    return render(request, 'boardapp/posts.html', post_dict)


def PostDetailView(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {'post': post, 'commentuploadform': CommentUploadForm()}

    return render(request, 'boardapp/post_detail.html', data)


def PostUploadView(request):
    if request.method == "GET":
        form = {"form": PostUploadForm()}

        return render(request, 'boardapp/post_upload.html', form)

    if request.method == "POST":
        form = PostUploadForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('boardapp:index')


def CommentUploadView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    form = CommentUploadForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return redirect('boardapp:detail', post_id=post_id)
