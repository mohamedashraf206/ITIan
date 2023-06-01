from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def courselist(request):
    courses = [(1, 'JAVA'), (2, 'Python'), (3, 'Dotnet')]
    context={}
    context['courses']=courses
    return render(request, 'course/course_list.html',context)


def courseadd(request):
    return render(request, 'course/add_course.html')


def courseupdate(request, id):
    return HttpResponse(' hi from course update view')


def coursedelete(request, ID):
    return HttpResponse(' hi  course with ID ' + str(ID) + ' is deleted')
