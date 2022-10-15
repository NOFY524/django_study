from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewPostForm
from account.models import User

# Create your views here.


def index(request):
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

            return render(request, 'post/main.html')

        else:
            return redirect('account:login')

