from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
        return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def Registration(request):
    if request.method == 'POST':
        Userid = request.POST['User id']
        Email = request.POST['Email']
        Password = request.POST['Password']

        user = User.objects.create_user(username=Userid,email=Email,password=Password)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request,'Registration.html')

def contact(request):
    return render(request,'contact.html')