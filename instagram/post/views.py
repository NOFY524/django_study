from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import NewPostForm, CommentForm
from account.models import User
from django.db.models import Q
from .models import Post, Comment
from . import serializers

# Create your views here.


def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = get_object_or_404(User, pk=request.user.id)
            following_users = user.following.all()
            posts = Post.objects.filter(
                Q(author__in=following_users) | Q(author=user)
            )
            serializer = serializers.PostSerializer(posts, many=True)

            print(serializer.data, 'printed')

            return render(request, 'post/main.html', {'posts': serializer.data, 'comment_form': CommentForm()})
    return render(request, 'post/main.html')


def new_post(request):
    if request.method == 'GET':
        form = NewPostForm()
        return render(request, 'post/new_post.html', {'form': form})

    elif request.method == "POST":
        if request.user.is_authenticated:
            user = get_object_or_404(User, pk=request.user.id)
            form = NewPostForm(request.POST, request.FILES)
            #print(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = user
                post.save()

            else:
                print(form.errors)

            return redirect(reverse('post:index'))

        else:
            return redirect('account:login')


def new_comment(request, post_id):
    #print("al;jkafkjl;fdskjl;afsdjkl;")
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        form = CommentForm(request.POST)
        print(request, request.POST, 'printed')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.posts = post
            comment.save()

            return redirect(reverse('post:index')+"#comment-"+str(comment.id))
    else:

        return redirect(reverse('account:login'))


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        return redirect(reverse('post:index'))
    else:
        return redirect(reverse('account:login'))


def post_like(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect(reverse('post:index'))
    else:
        return redirect(reverse('account:login'))
