from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Contact

# Create your views here.
def home(request):

    import requests
    import json

    news_api_request = requests.get(
        "https://newsapi.org/v2/everything?q=tesla&from=2021-03-18&sortBy=publishedAt&apiKey=9af417b71f8a45248f70d19a18e7728d"    
    )
    api = json.loads(news_api_request.content)

    return render(request,'home.html',  {'api':api})

def about(request):
    return render(request,'about.html')

def login(request):
    if request.method == 'POST':
        Userid = request.POST['User id']
        Password = request.POST['Password']

        user = auth.authenticate(username=Userid, password=Password)

        if user is not None :
            auth.login(request, user)
            return redirect('/')

        else :
            messages.info(request, "Invalid credential")
            return redirect('Registration.html')
    else :
        return render(request, 'Registration.html')

def register(request):
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
    if request.method == 'POST':
        contact = Contact()
        FirstName = request.POST['First Name']
        LastName = request.POST['Last Name']
        Email = request.POST['Email']
        MobileNumber = request.POST['Mobile Number']
        Message = request.POST['Message']
        
        contact.firstName = FirstName
        contact.lastName = LastName
        contact.email = Email
        contact.mobileNo = MobileNumber
        contact.message = Message

        contact.save();
        return redirect('/')

    else :
        return render(request,'contact.html')