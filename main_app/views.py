from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 
from .models import Patient, Doctor, Appointment

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dash_index(request):
    return render(request, 'dashboard/index.html')

def appointments_index(request):
    appts = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/index.html', {'appts': appts})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign-up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)