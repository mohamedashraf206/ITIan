from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import *


# Create your views here.

def Login(req):
    context={}
    if (req.method=='POST'):
        info_valid=trainee_info.objects.filter(email=req.POST['email'],password=req.POST['password'])
        if (len(info_valid) != 0):
            req.session['firstname']=info_valid[0].firstname
            return HttpResponseRedirect('/userinfo')
        else:
            context['invalid'] = 'the email address is not exist plz enter valid email '

    return render(req, 'Login.html' ,context=context)


def Registration(req):
    context = {}
    if (req.method == 'POST'):
        firstname = req.POST['firstname']
        email = req.POST['email']
        password = req.POST['password']
        train = trainee_info(firstname=firstname)
        train.email = email
        train.password = password
        train.save()
    return render(req, 'register.html', context)


def Logout(req):
    req.session.clear()
    return HttpResponse('Logout')


def userinfo(request):
    if ('firstname' in request.session):
        context={}
        context['trainee_db'] = trainee_info.objects.all()
        return render(request,'user.html' ,context)
    else:
        return HttpResponseRedirect('/')


