from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')

@login_required(login_url="/accounts/login/") # redirect to login page if not logged in
def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')