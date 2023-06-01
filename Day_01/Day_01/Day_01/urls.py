"""
URL configuration for Day_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from trainee.views import *
from course.views import *
from myaccount.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #trainee route
    path('trainee/',traineelist,name='traineelist'),
    path('trainee/add',traineeadd,name='traineeadd'),
    path('trainee/update/<int:id>',traineeupdate,name='traineeupdate'),
    path('trainee/delete/<int:ID>', traineedelete, name='traineedelete'),
    #course route
    path('course/', courselist, name='courselist'),
    path('course/add', courseadd, name='courseadd'),
    path('course/update/<int:id>', courseupdate, name='courseupdate'),
    path('course/delete/<int:ID>', coursedelete, name='coursedelete'),
    #myaccount route
    path('',Login , name='Login'),
    path('Registration',Registration , name='Registration'),
    path('Logout',Logout , name='Logout'),
]
