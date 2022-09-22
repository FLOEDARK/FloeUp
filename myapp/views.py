from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Feature, About, FloeAbout, Contact
from django.contrib import messages

# Create your views here.

def index(request):
   #floeup= {
    #  'floeabout' : FloeAbout.objects.all(),
     # 'features' : Feature.objects.all()
   #}
   features = Feature.objects.all()
   floeabout= FloeAbout.objects.all()
   contact= Contact.objects.all()
   return render(request, 'index.html', {'floeup' : floeabout, 'features':features, 'contact': contact})
   


#def floeup(request):
 #  floeabout= FloeAbout.objects.all()
  # return render(request, '')

def counter(request):
   posts= [1, 2, 3, 4, 5, 'Emmanuel', 'Tom']  
   return render(request, 'counter.html', {'posts': posts})

def register(request):
   if request.method== 'POST':
      username= request.POST['username']
      email= request.POST['email']
      password= request.POST['password']
      password2= request.POST['password2']

      if password == password2:
         if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Used.')
            return redirect('registers')
         elif User.objects.filter(username=username).exists():
            messages.info(request, 'username Already Used')
            return redirect('register')
         else:
            user= User.objects.create_user(username=username, email=email, password=password)
            user.save();
            return redirect('login')

      else:
         messages.info(request, 'Password Not The Same')
         return redirect('register')
      
   else:
      return render(request, 'register.html')


def login(request):
   if request.method =='POST':
      username  =request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
         auth.login(request, user)
         return redirect('/')
      else:
         messages.info(request, 'Credentials invalid!')
         return redirect('login')

   else:
      return render(request, 'login.html') 

def about(request):
   about = About.objects.all()
   return render(request, 'index.html','about.html',{'about': about})

def logout(request):
   auth.logout(request)
   return redirect('/')

def post(request, pk):
   return render(request, 'post.html', {'pk' : pk})

def services(request):
   return render(request, 'services.html')

def details(request):
   return render(request, 'details.html')

def contact(request):
   return render(request, 'contact.html')

def pricing(request):
   return render(request, 'pricing.html')

