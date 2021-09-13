from django.shortcuts import render, redirect
from .form import UserRegisterForm 
from django.contrib.auth.models import User
from django.contrib import messages



def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account created successfully. Kindly login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'accounts/register.html', {'form':form})

