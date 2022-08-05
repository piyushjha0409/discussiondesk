# from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from myapp.models import contact

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def handleSignup(request):
    #getting post parameters 
    if request.method == 'POST':
        username = request.POST['username']
        first = request.POST['first']
        last  = request.POST['last']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

    #checks
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')

    #creating user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first 
        myuser.last_name = last 
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        send_mail(
        'Signed Up Successfully',
        'Welcome to Discussion Desk, You have successfully Signed up to the Discussion Desk. \n\n\nDiscussion Desk of IITM serves as a resource to help students of IITM on programming and help them prepare for coding interview. Students can ask anything related to programming. Experts at Coding Forum provide programming problems of different difficulty levels. Students can post their answers which are evaluated by experts. Students are encouraged to clear their doubts by participating in discussions. Also, students can read discussions on different programming languages such as C, C++, PHP, Python, JavaScript, and much more.\n\n\n\nRegards\n\nDiscussion Desk (IITM)',
        'discussion.desk.iitm@gmail.com',
        [email],
        fail_silently=False,
        )
        return redirect('/')
    else:
        return HttpResponse('Not Allowed')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username= loginusername, password= loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid LogIn Credentials")
            return redirect('/')
    return HttpResponse("404- Not found")

def handleLogout(request):

    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')

def Contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      content = request.POST.get('content')
      Contact = contact(name = name, email = email, phone = phone, content = content)
      Contact.save()
      messages.info(request, "Successfully Sent Your Query")
    return render(request, 'myapp/contact.html')


