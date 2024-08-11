from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .models import User

from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'users/user-list.html', context)


class UserDetailView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        context = {'user': user}
        return render(request, 'users/user-detail.html', context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/user-login.html', context)

    def post(self, request):
        form = AuthenticationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('books:book-list')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'users/user-login.html', context)


class UserLogoutView(View):
    def get(self, request):
        messages.info(request, 'You are now logged out')
        logout(request)
        return redirect('books:book-list')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'users/user-register.html', context)

    def post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('users:user-login')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'users/user-register.html', context)


class UserUpdateView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        form = UserUpdateForm()
        context = {'form': form}
        return render(request, 'users/user-update.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            form = UserUpdateForm(request.POST or None, request.FILES, instance=user)
            context = {'form': form}
            if form.is_vaid():
                form.save()
                login(request, user)
                messages.success(request, f'Account updated for {form.cleaned_data["username"]}')
                return redirect('users:user-detail')
            return render(request, 'users/user-update.html', context)
        else:
            messages.error(request, 'You are not logged in')
            return redirect('books:book-list')

