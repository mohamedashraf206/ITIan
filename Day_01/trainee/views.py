

from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *
from .form import *


# Create your views here.
def traineelist(request):

    context={}
    context['trainee_list'] = trainee_list.objects.all()
    return render(request,'trainee/trainee_list.html',context)
def traineeadd(req):
    context={}
    if (req.method == 'POST'):
        trainee_name = req.POST['mytrainee']
        email = req.POST['email']
        train = trainee_list(trainee_name=trainee_name)
        train.trainee_email = email
        train.save()
    return render(req,'trainee/add_trainee.html',context)
def traineeupdate(req,id):
    context = {}
    context['catagories'] = trainee_list.objects.all
    context['taskdata'] = trainee_list.objects.get(id=id)
    if (req.method == 'POST'):
        name = req.POST['taskname']
        trainee_list.objects.filter(id=id).update(name=req.POST['taskname'],
                                          catagoryid=Catagory.objects.get(id=req.POST['catagory']))
        return HttpResponseRedirect('/Tasks')
    return HttpResponse(' hi from trainee update view')
def traineedelete(request,ID):
    trainee_list.objects.filter(id=ID).delete()



    return HttpResponseRedirect('/trainee')



    # return HttpResponse(' hi  trainee with ID ' +str(ID)+ ' is deleted')



def add_trainee_form(req):
    tr = myadd_trainee_form()
    context = {}
    context['trainee_form'] = tr
    if(req.method=='POST'):
        trainee_email = req.POST['trainee_email']
        trainee_name = req.POST['trainee_name']
        trainee_list.objects.create( trainee_email=trainee_email,trainee_name=trainee_name )

    return render(req,'trainee/addTraineeForm.html',context)
