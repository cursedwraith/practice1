from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return render(request, 'first/index.html')
    return HttpResponse("Hello, world. You're at the first index.")
