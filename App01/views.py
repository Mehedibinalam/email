from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Trainee
from .forms import TraineeForm

# Create your views here.

def show(request):
    trainees = Trainee.objects.all()
    return render(request, "show.html", {'trainees':trainees})

def deleteRecord(request, id):
    trainee = Trainee.objects.get(TraineeID=id)
    trainee.delete()
    return redirect("/")

def emailSend(request):
    subject = "Due's Payment Notification"
    msg = "Please pay your Due amount within 20 days"
    to = []
    for trn in Trainee.objects.all():
        if trn.DueAmount>0:
            to.append(trn.EmailAddress)
        else:
            pass
    res = send_mail(subject, msg, EMAIL_HOST_USER, to, fail_silently=False)
    if res ==1:
        msg = "Your Email Sent Successfully"
    else:
        msg = "Your Email Could not Sent!!!"
    return HttpResponse(msg)