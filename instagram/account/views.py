from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm


def signup(request):
    if request.method == 'GET':
        form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('post:index')

    return render(request, 'account/signup.html', {'form': form})
