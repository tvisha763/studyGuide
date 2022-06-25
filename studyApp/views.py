from django.shortcuts import render
from contextvars import Context
from operator import contains
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
import requests
import urllib
import os
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import User, Post
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password').encode("utf8")
        confirmPass = request.POST.get('confirmPass').encode("utf8")
        inputs = [email, username, password, confirmPass, phone]

        # checking if confirm password matches password   
        if (password != confirmPass):
            messages.error(request, "The passwords do not match.")
            return redirect('signup')

        for inp in inputs:
            if inp == '':
                messages.error(request, "Please fill all the boxes.")
                return redirect('signup')

        if password != '' and len(password) < 6:
            messages.error(request, "Your password must be at least 6 charecters.")
            return redirect('signup')
        

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists. If this is you, please log in.")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "An account with this username already exists. Please pick another one.")
            return redirect('signup')

        else:
            salt = bcrypt.gensalt()
            user = User()
            user.email = email
            user.username = username
            user.phone = phone
            user.password = bcrypt.hashpw(password, salt)
            user.salt = salt
            user.save()
            return redirect('login')
    else:
        if request.session.get('logged_in'):
            return redirect('dashboard')

    return render(request, 'auth/signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password').encode("utf8")
        inputs = [email, password]

        for inp in inputs:
            if inp == '':
                messages.error(request, "Please fill all the boxes.")
                return redirect('login')

        if "@" not in email:
            messages.error(request, "Please enter your email address.")
            return redirect('login')

        if User.objects.filter(email=email).exists():
            saved_hashed_pass = User.objects.filter(email=email).get().password.encode("utf8")[2:-1]
            saved_salt = User.objects.filter(email=email).get().salt.encode("utf8")[2:-1]
            user  = User.objects.filter(email=email).get()
            request.session["username"] = user.username
            request.session['logged_in'] = True
           
            salted_password = bcrypt.hashpw(password, saved_salt)
            if salted_password == saved_hashed_pass:
                return redirect('dashboard')
            else:
                messages.error(request, "Your password is incorrect.")
                return redirect('login')

        else:
            messages.error(request, "An account with this email does not exist. Please sign up.")
            return redirect('login')

    else:
        if request.session.get('logged_in'):
            return redirect('dashboard')

    return render(request, 'auth/login.html')

def logout(request):
    if not request.session.get('logged_in') or not request.session.get('username'):
        return redirect('login')
    else:
        request.session["username"] = None
        request.session['logged_in'] = False
        return redirect('login')


def dashboard(request):
    return render(request, 'dashboard.html')

def post(request):
    
        return render(request, 'post.html')

def createPost(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    if request.method == "POST":
        user = User.objects.get(username=request.session["username"])
        postType = request.POST.get('postType')
        materialName = request.POST.get('materialName')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        pracFile = request.FILES.get('pracFile')
        subjectPrac = request.POST.get('subject')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        subjectsTutor = request.POST.get('subjects')
        rate = request.POST.get('rate')
        descriptionSale = request.POST.get('descriptionSale')
        descriptionPrac = request.POST.get('descriptionPrac')
        descriptionTutor = request.POST.get('descriptionTutor')

        print(price)
        
        if postType == "1":
            print("works")
            inputs = [image, materialName, postType, price, descriptionSale]
            for inp in inputs:
                if inp == '' or inp == None:
                    messages.error(request, "Please fill all the boxes.")
                    return redirect('post')

            post = Post(image=image, materialName=materialName, postType=postType, price=price, description=descriptionSale, user=user)
            post.save()
            return redirect('dashboard')
        elif postType == "2":
            inputs = [pracFile, subjectPrac, postType, descriptionPrac]
            for inp in inputs:
                if inp == '' or inp == None:
                    messages.error(request, "Please fill all the boxes.")
                    return redirect('post')
            post = Post(pracFile=pracFile, subjectPrac=subjectPrac, postType=int(postType), description=descriptionPrac, user=user)
            post.save()
            return redirect('dashboard')
        elif postType == "3":
            inputs = [fname, lname, subjectsTutor, postType, descriptionTutor]
            for inp in inputs:
                if inp == '' or inp == None:
                    messages.error(request, "Please fill all the boxes.")
                    return redirect('post')
            post = Post(fname=fname, lname=lname, subjectsTutor=subjectsTutor, postType=int(postType), description=descriptionTutor, user=user, rate=rate)
            post.save()
            return redirect('dashboard')
        else:
            messages.error(request, "Please select a post type")
            return render(request, 'post.html')
    else:
        return render(request, 'post.html')


def salePage(request):
        if not request.session.get('logged_in'):
            return redirect('/login')
        if request.method == "GET":
            info = Post.objects.filter(postType=1)
            print (info[0].image.url)
            context = {'details': info}
            return render(request, 'salePage.html', context)
        
def materialSearch(request):
    if not request.session.get('logged_in'):
        return redirect('/login')
    if request.method == "GET":
        Searched = request.GET.get("materialFilter")
        info = Post.objects.filter(materialName__contains=Searched)    
        context={'details' : info.filter(postType=1)}
        return render(request, 'salePage.html', context)
