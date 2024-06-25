from django.http import HttpResponse
from django.shortcuts import render

 

def index(request):
    context = {
        'title': "Home",
        'content': "Main page",
        
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "About us",
        'content': "About",
        "text_on_page": "Text about how good is this shop"
    }

    return render(request, 'main/about.html', context)
    