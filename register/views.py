from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm
from django.urls import reverse
from django.contrib.auth import logout as lt
from main.models import Author

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect(reverse('home'))
    context.update({
        "form":form,
        "title": "signup",
    })
    return render(request, 'register/signup.html', context)

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = user, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
    context.update({
        "form":form,
        "title": "signin",
    })
    return render(request, 'register/signin.html', context)


@login_required
def logout(request):
    lt(request)
    return redirect('home')


@login_required
def pers(request):
    context = {}
    user = request.user
    username = request.user.username

    author, created = Author.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdateForm(instance=author)

    context.update({
        "form": form,
        'user': user,
        "title": "Update Profile",
    })
    return render(request, 'register/pers.html', context)