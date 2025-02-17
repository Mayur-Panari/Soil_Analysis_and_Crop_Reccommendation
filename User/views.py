from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from urllib import request
from django.contrib import messages
from User.helper import GETDATA

from User.models import Feedback




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





def about(request):
    return render (request,"about.html")

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