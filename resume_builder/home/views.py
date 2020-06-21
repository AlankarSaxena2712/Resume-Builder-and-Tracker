from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

# Create your views here.
def home(request):
    return render(request, 'index.html')

def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        register_as = request.POST.get('register_as')
        
        if pass1 == pass2:
            if register_as == 'student_register':
                new_user = User.objects.create_user(username, email=None, password = pass1)
                add_user_group = Group.objects.get_by_natural_key('resume')
                add_user_group.user_set.add(new_user)
                new_user.save() 
                messages.success(request, f"{username} Registered Successfully")
                return redirect('home')
            else:
                messages.warning(request, "Please select whether to register as Student or Company")
                return redirect('home')
        else:
            messages.error(request, "Please check your password! They don't match")
            return redirect('home')
    else:
        return redirect('home')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('resume_personal')
        else:
            messages.error(request, "Invalid Credentials, Please Check your Username and Password")
    return HttpResponse("404 - Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')