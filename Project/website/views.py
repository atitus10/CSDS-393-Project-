from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

def index(request):
    return HttpResponse("Hello, world. You're at the website index.")


# Create your views here.
def register(response):
    if response.method == "POST":
    	form = RegisterForm(response.POST)
    	if form.is_valid():
    	    form.save()

    	return redirect("/home")
    else:
	    form = RegisterForm()

    return render(response, "register/register.html", {"form":form})