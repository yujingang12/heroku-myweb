from django.shortcuts import render, redirect
#회원가입 여기에 하겠슴다!
from django.contrib import auth
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
#
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'account/signup.html', {'form': form})

#로그인
def login(requset):
    if requset.method == 'POST':
        form = AuthenticationForm(data=requset.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(requset,user)
            return redirect('main')
        else:
            return render(requset, 'account/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(requset, 'account/login.html', {'form':form})

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('main')
