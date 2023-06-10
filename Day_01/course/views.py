
# from django.shortcuts import render
# from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view
from .models import *
from .serilaizer import *


# Create your views here.
@api_view(['GET'])
def courselist(request):
   my_courses = courses.objects.all()
   if(my_courses):
        my_courses_serialized = courses_serializer(my_courses, many=True)
        return Response(data=my_courses_serialized.data)
    # return render(request, 'course/course_list.html',context)


@api_view(['GET'])
def get_course(request , id):
   getCourse = courses.objects.get(id=id)
   if (getCourse is not None):
      return Response(data= courses_serializer(getCourse).data )
   else:
       return Response (status=HTTP_404_NOT_FOUND)



@api_view(['POST'])
def add_course(request) :
    courses.objects.create(course_name=request.data['name'] , course_capacity=request.data['capacity'])

    return Response(HTTP_200_OK)

@api_view(['PUT'])
def update_course(request , id):
    if (len(courses.objects.filter(id=id))!=0):

        updateCourse= courses.objects.get(id=id)
        serializedUpdateCourse= courses_serializer(instance=updateCourse,data=request.data)

        if (serializedUpdateCourse.is_valid()):
            serializedUpdateCourse.save()
            return Response(status=HTTP_200_OK, data=serializedUpdateCourse.data)
    else:
        return Response(status=HTTP_207_MULTI_STATUS)


@api_view(['DELETE'])
def delete_course (request , id ):
    data = courses.objects.get(id=id)
    data.delete()
    return Response (status=HTTP_200_OK)

# def courseadd(request):
    # return render(request, 'course/add_course.html')


# def courseupdate(request, id):
    # return HttpResponseRedirect('/course')


# def coursedelete(request, ID):
    # return HttpResponse(' hi  course with ID ' + str(ID) + ' is deleted')
