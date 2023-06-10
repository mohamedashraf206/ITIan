from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def traineelist(request):
    trainee = [(1, 'mohamed'), (2, 'Eslam'), (3, 'Tarek')]
    context={}
    context['trainee']=trainee
    return render(request,'trainee/trainee_list.html',context)
def traineeadd(request):
    return render(request,'trainee/add_trainee.html')
def traineeupdate(request,id):
    return HttpResponse(' hi from trainee update view')
def traineedelete(request,ID):
    return HttpResponse(' hi  trainee with ID ' +str(ID)+ ' is deleted')