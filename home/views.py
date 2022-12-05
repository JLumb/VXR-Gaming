from django.shortcuts import render

# Create your views here.

def index(request):
    """ a view to return home page """
    
    return render(request, 'home/index.html')