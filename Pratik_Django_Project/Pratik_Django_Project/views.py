from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'title' : 'Home Page',
    }
    return render(request,"index.html", data)

# def home(request):
#     return render(request,"index.html")

def aboutus(request):
    return HttpResponse("<h1 style = 'color:indigo'> welcome to my First Web Page 'AboutUS' </h1>")

def cource(request):
    return HttpResponse("<h1 style = 'color:powderblack'> welcome to my First Web Page 'Cource' </h1>")

def courceDetails(request,courceid):
    return HttpResponse(courceid)