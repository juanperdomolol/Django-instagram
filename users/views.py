"""USER VIEWS"""

#django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

#Exception
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile

#Forms 
from users.forms import ProfileForm
# Create your views here.

def update_profile(request):
    """ Update a user's profile view """
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            messages.success(request, 'Your profile has been updated!')
            
            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form
            }
        )

def login_view(request):
    """login view. """ 
    if request.user.is_authenticated:
            redirect("posts")
            
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('/posts')
        else:
            return render(request, 'users/login.html',{'error':'Invalid Username or Password'})

        
       
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """logout_view """
    logout(request)
    return redirect('login')

def signup(request):
    """sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd'] 
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html',{'error':'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username= username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'Username is already '})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')