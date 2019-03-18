from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm #Built-in model form(User model)which is exist in django we can create our own form

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)   #This is FBV signup
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        else:
            return render( request, 'accounts/signup.html', context={"form":form})

    form = UserCreationForm()
    return render(request, 'accounts/signup.html',context={'form':form})

#Note
# we dint need to write login and logout view ouself.
# we can use django login logout by defining LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_ URL
#For this we needto add 'path('accounts/', include('django.contrib.auth.urls')),' in main urls.py


"""
def signup(request):  #If we use this function the passwords are visible on the screen While typing
    if request.method == 'POST':
        if request.POST['Password1'] == request.POST['Password2']:

            try:
                user = User.objects.get(username = request.POST['Username'])
                return render(request,'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['Username'], password = request.POST['Password1'])
                login(request, user)
                #return render(request,'accounts/signup.html')
                return redirect('home')
        else:
            return render(request,'accounts/signup.html', {'error':'Passwords didn\'t match'})

    else:
        return render(request, 'accounts/signup.html')

def loginView(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['Username'], password=request.POST['Password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')

        else:
            return render(request,'accounts/login.html', {'error':'Username and Password didn\'t match'})

        #else:
            #return render(request,'accounts/login.html', {'error':'Passwords didn\'t match'})

    else:
        return render(request, 'accounts/login.html')

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
"""
