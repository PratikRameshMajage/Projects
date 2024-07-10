#########################################

$$$$$$$$$$$$$$$___BASIC INSTALLATION COMMANDS____$$$$$$$$$$$$$$$


<!-- pip install django -->
<!-- pip freeze -->
<!-- django-admin startproject myproject -->
<!-- python manage.py runserver  -->
<!-- localhost:8000 -->
<!-- localhost:8000/admin -->
<!-- python manage.py make migration -->
<!-- python manage.py migrate -->
<!-- python manage.py createsuperuser -->

#########################################

$$$$$$$$$$$$$$$___URLS____$$$$$$$$$$$$$$$
<!-- from django.contrib import admin
from django.urls import path -->
<!-- from Pratik_Django_Project import views -->

<!-- urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/',views.aboutus),
    path('cource/',views.cource),
    path('cource/<slug:courceid>',views.courceDetails),
] -->


#########################################

$$$$$$$$$$$$$$$___VIEWS____$$$$$$$$$$$$$$$

<!-- from django.http import HttpResponse
from django.shortcuts import render -->

<!-- def home(request):
    data = {
        'title' : 'homepage',
    }
    return render(request,"index.html", data) -->

<!-- def home(request):
    return render(request,"index.html")

def aboutus(request):
    return HttpResponse("<h1 style = 'color:indigo'> welcome to my First Web Page 'AboutUS' </h1>")

def cource(request):
    return HttpResponse("<h1 style = 'color:powderblack'> welcome to my First Web Page 'Cource' </h1>")

def courceDetails(request,courceid):
    return HttpResponse(courceid) -->
 -->

#########################################

$$$$$$$$$$$$$$$___TEMPLATES____$$$$$$$$$$$$$$$

[<!-- 'DIRS': [BASE_DIR,"templates"], -->]

#########################################

$$$$$$$$$$$$$$$__DYNAMIC_CHANGE_DATA____$$$$$$$$$$$$$$$

[<!-- <title>{{title}}</title> --> 
=====
<!-- def home(request):
    data = {
        'title' : 'homepage',
    }
    return render(request,"index.html", data) -->]
