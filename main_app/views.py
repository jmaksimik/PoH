from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def dash_index(request):
    return render(request, 'dashboard/index.html')

def appointments_index(request):
    return render(request, 'appointments/index.html')