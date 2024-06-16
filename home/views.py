from django.shortcuts import render


def home(request):
    template_name = 'home/index.html' 
    
    return render(request, template_name)