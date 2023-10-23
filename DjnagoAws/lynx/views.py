from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User

from .forms import CreateUserForm , LoginUserForm , UpdateUserForm , UpdateProfileForm
from .models import Profile



@login_required(login_url='my-login')
def profile_management(request):
    

    profile = Profile.objects.get(user= request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance= request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES , instance= profile)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')
        
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    
    else:
        user_form = UpdateUserForm(instance= request.user)
        profile_form = UpdateProfileForm(instance= profile)

    

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'lynx/profile-management.html', context=context)



def index(request):
    
    return render(request, 'lynx/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            current_user = form.save(commit=False)
            form.save()
            profile = Profile.objects.create(user=current_user)
            return redirect('my-login')
    else:
        form = CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'lynx/register.html', context= context)



def my_login(request):
    
    if request.method == 'POST':
        form = LoginUserForm(request, data= request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = LoginUserForm()

    context = {
        'form': form
    }
    return render(request, 'lynx/my-login.html', context=context)


def user_logout(request):
    
    auth.logout(request)
    return redirect('index')



@login_required(login_url='my-login')
def dashboard(request):
    
    profile = Profile.objects.get(user = request.user)

    context= {
        'profile': profile
    }
    return render(request, 'lynx/dashboard.html', context=context)




def delete_user(request):

    if request.method == 'POST':
        user =  User.objects.get(username =  request.user )
        user.delete()
        return redirect('index')


    context = {}
    return render(request, 'lynx/delete_user.html', context=context)
    