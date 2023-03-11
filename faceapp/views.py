from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html",{ "msg" :"Faceclone made by - Soumya"})

def home(request):
    user = request.user
    if user.is_anonymous:
        return render(request,"index.html")
    else:
        pro = UserProfile.objects.get(user=user)
        status = pro.status
        
        firstname = user.first_name
        lastname = user.last_name
        fullname = firstname+" "+lastname
        return render(request,"home.html",{"name":fullname,"status":status})

def profile(request):
    user = request.user
    if user.is_anonymous:
        return render(request,"index.html")
    else:
        pro = UserProfile.objects.get(user=user)
        location = pro.location
        status = pro.status
        
        firstname = user.first_name
        lastname = user.last_name
        fullname = firstname+" "+lastname
        return render(request,"profile.html",{"name":fullname,
        "location":location,"status":status,"pic":pro.pic})

def Login(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return redirect("index")
    else:
        return render(request,"index.html")

def Logout(request):
    logout(request)
    return redirect("index")


def Register(request):
    if request.method == "POST":

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        location = request.POST["location"]
        password = request.POST["password"]
        username = request.POST["username"]

        user = User.objects.create_user(username=username, first_name=firstname , last_name=lastname)
        user.set_password(password)
        user.is_staff = True
        user.save()
        u = UserProfile(user=user,location=location)
        u.save()

        return redirect("Resindex")
        
def Resindex(request):
    
    return render(request,"index.html",{ "msg" :"REgistration Complete"})

def Post(request):
    if request.method == "POST":
        user = request.user
        content = request.POST["content"]
        pro = UserProfile.objects.get(user=user)
        status = pro.status
        
        firstname = user.first_name
        lastname = user.last_name
        fullname = firstname+" "+lastname
        return render(request,"home.html",{"name":fullname,"status":status,"content":content})