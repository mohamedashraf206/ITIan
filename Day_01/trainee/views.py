from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def traineelist(request):
    return render(request, 'trainee/trainee_list.html')


def traineeadd(request):
    return render(request, 'trainee/add_trainee.html')


def traineeupdate(request, id):
    return HttpResponse(' hi from trainee update view')


def traineedelete(request, ID):
    return HttpResponse(' hi  trainee with ID ' + str(ID) + ' is deleted')
