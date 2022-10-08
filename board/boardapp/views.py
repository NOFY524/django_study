from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Post, Comment
from .forms import PostUploadForm, CommentUploadForm

from django.contrib.auth.decorators import  login_required

# Create your views here.


def index(request):
    post_list = Post.objects.order_by('-create_time')
    post_dict = {'post_list': post_list}

    return render(request, 'boardapp/posts.html', post_dict)


def PostDetailView(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {'post': post, 'commentuploadform': CommentUploadForm()}

    return render(request, 'boardapp/post_detail.html', data)


@login_required(login_url="accounts:login")
def PostUploadView(request):
    if request.method == "GET":
        form = {"form": PostUploadForm()}

        return render(request, 'boardapp/post_upload.html', form)

    if request.method == "POST":
        form = PostUploadForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
        return redirect('boardapp:index')


@login_required(login_url="accounts:login")
def CommentUploadView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    form = CommentUploadForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user

        comment.save()

    return redirect('boardapp:detail', post_id=post_id)


@login_required(login_url="accounts:login")
def PostDeleteView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        print('checked')
        return redirect('boardapp:detail', post_id=post.id)
    print('checked 2')
    post.delete()
    return redirect('boardapp:index')


@login_required(login_url="accounts:login")
def CommentDeleteView(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        return redirect('boardapp:detail', post_id=post_id)
    comment.delete()
    return redirect('boardapp:detail', post_id=post_id)


@login_required(login_url='accounts:login')
def PostLikeView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.likes_user.all():
        post.likes_user.remove(request.user)
    else:
        post.likes_user.add(request.user)

    return redirect('boardapp:detail', post_id=post.id)


@login_required(login_url='accounts:login')
def CommentLikeView(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user in comment.likes_user.all():
        comment.likes_user.remove(request.user)
    else:
        comment.likes_user.add(request.user)
    return redirect('boardapp:detail', post_id=post_id)
