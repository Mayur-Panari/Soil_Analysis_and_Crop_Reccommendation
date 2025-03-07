from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from urllib import request
from django.contrib import messages
from User.helper import GETDATA
from User.models import Feedback




def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('signin')

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "signin.html")



@login_required
def index(request):

    data_getter = GETDATA()

    if request.method == "POST":

        input_data = {
                        'nitrogen':request.POST.get('nitrogen'),
                        'potassium':request.POST.get('potassium'),
                        'phosphorus':request.POST.get('phosphorus'),
                        'humidity':request.POST.get('humidity'),
                        'ph':request.POST.get('ph'),
                        'rainfall':request.POST.get('rainfall'),
                        'temperature':request.POST.get('temperature')
                    }

        print("Data",input_data)
        prediction = data_getter.get_prediction(input_data)
        return JsonResponse(prediction)

    return render (request,"index.html")





@login_required
def about(request):

    return render (request,"about.html")

@login_required
def feedback(request):

    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone=request.POST.get('phone')
        description =request.POST.get('description')
        feedbacks=Feedback(name=name , email=email,phone=phone,description=description)
        feedbacks.save()
        messages.success(request, "Your feedback has been submitted successfully!")


    return render (request,"feedback.html")


def logout(request):
    django_logout(request)

    return redirect('signin')
