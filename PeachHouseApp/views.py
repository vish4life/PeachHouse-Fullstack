from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    message="Welcome to Peach House"
    # return HttpResponse(message)
    return render(request,'index.html',{})