from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login  , logout 
from django.contrib import messages
from.models import contact_us_feedback
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def home(request):
    return render(request,"home.html")
def pricing(request):
    return render(request,"pricing.html")
def syntax(request):
    return render(request,"syntax.html")

def indicator_store(request):
    return render(request,"indicator_store.html")
def symbol(request):
    return render(request,"symbol.html")
def video(request):
    return render(request,"video.html")
def faq(request):
    return render(request,"faq.html")

def user_details(request):
    
    if request.method =="POST":
        first_name = request.POST['first_name1']
        last_name = request.POST['last_name1']
        phone_number = request.POST['phone_number']
       
        usr = User.objects.get(id=request.user.id)
        usr.first_name=first_name
        usr.last_name=last_name
        usr.Mobile_number=phone_number
        usr.save()
        
    
        messages.success(request, 'Your profile has been updated')
        return render(request, 'user_profile.html')
    return render(request, 'user_profile.html')

def signup(request):
    if request.method == 'POST':
     username = request.POST['username']
     email = request.POST['email']
     inputphone = request.POST['inputphone']
     password = request.POST['pass']
     cpassword = request.POST['cpass']
     if User.objects.filter(username = username).exists():
      print('username already taken')
     elif username == '' or email == '' or password == '':
      print("empty")
     elif password != cpassword:
      messages.error(request, "Password not match")
     else:
      users = User.objects.create_user(username = username, email = email, Mobile_number=inputphone , password =password)
      users.save()
      messages.success(request, "You have succesfully account")
      return redirect('login')
    else:
     return render(request, 'signup.html')
    return render(request, "signup.html")


def loginuser(request):
    if request.method == 'POST':
     username = request.POST['uname']
     password = request.POST['pass']
     user = authenticate(request, username=username, password = password)
     if user is not None:
      login(request, user)
      messages.success(request, 'successfully login')
      return redirect('dashboard')
     else:
      messages.error(request, "invalid usernames ")
    else:
      return render(request, 'login.html')
    return render(request, "login.html")


def logoutuser(request):
  logout(request)
  messages.success(request, "You have succesfully logout")
  return redirect('/')

def dashboard(request):
  return render(request, 'dashboard.html')


  

def contact_us(request):
   if request.method=="POST":
     c_name=request.POST["c_name"]
     c_email=request.POST["c_email"]
     c_number=request.POST["c_number"]
     c_experience=request.POST["c_experience"]
     c_wnumber=request.POST["c_wnumber"]
     c_country=request.POST["c_country"]
     c_message=request.POST["c_message"]
     print(c_name,c_email,c_number,c_experience,c_wnumber,c_country,c_message)

     User_message=contact_us_feedback(
       c_name=c_name,
       c_email=c_email,
       c_number=c_number,
       c_experience=c_experience,
       c_wnumber=c_wnumber,
       c_country=c_country,
       c_message=c_message

     )
     User_message.save()
     messages.success(request, "You feedback has been sent, Our technical team get back to you asap")
     return render(request,"contact_us.html")


   return render(request,"contact_us.html")


def admin_panel(request):
  User_check = User.objects.all()
  User_contact_us_feedback = contact_us_feedback.objects.all()

  return render(request,"admin_panel.html",{"User_check":User_check,"User_contact_us_feedback":User_contact_us_feedback})


def delete_user(request,id):
  if request.method=="POST":
    Del_user=User.objects.filter(id=id)
    Del_user.delete()
    messages.success(request, "A user has been deleted")
    return redirect("admin_panel")
  
def delete_feedback(request,id):
  if request.method=="POST":
    del_contact_us_feedback=contact_us_feedback.objects.filter(id=id)
    del_contact_us_feedback.delete()
    messages.success(request, "Feedback has been deleted")
    return redirect("admin_panel")