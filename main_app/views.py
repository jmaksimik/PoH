from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView 
from django.contrib.auth import login, authenticate
from .models import Patient, Doctor, Appointment, Prescription, Insurance
from .models import Patient, Doctor, Appointment, Prescription, Document
from django.contrib.auth.models import User
from .forms import UserForm, PatientForm, PrescriptionForm, NewUserForm, SearchProvider, InsuranceForm
import requests
import json
from django.http import HttpResponse
import uuid 
import boto3 
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'pursuitofhealth'


# Create your views here.


def home(request):
    return render(request, 'home.html')

def dash_index(request):
    return render(request, 'dashboard/index.html')

def appointments_index(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/index.html', 
        {
            'appointments': appointments,
        })


def documents_index(request):
    return render(request, 'documents/index.html')


def prescriptions_index(request):
    prescriptions = Prescription.objects.all
    
    
    prescription_form = PrescriptionForm()

    return render(request, 'prescriptions/index.html',
        {
            'prescriptions': prescriptions,
            'prescription_form': prescription_form,
            
        })

def insurance_index(request):
    insurances = Insurance.objects.all
    insurance_form = InsuranceForm()
    return render(request, 'insurance/index.html', {'insurances': insurances, 'insurance_form': insurance_form,})

# User functionality

def update_profile(request):
    error_message = ''
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        patient_form = PatientForm(request.POST, instance = request.user.patient)
        if user_form.is_valid() and patient_form.is_valid():
            user_form.save()
            patient_form.save()
            return redirect('index')
        else:
            error_message = 'Invalid entries - please try again'
    else: 
        user_form = UserForm(instance=request.user)
        patient_form = PatientForm(instance=request.user.patient)
    return render(request, 'dashboard/profile.html', {
        'user_form': user_form,
        'patient_form': patient_form
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign-up - try again'
    form = NewUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class AppointmentDetail(DetailView):
    model = Appointment
    template_name = 'appointments/detail.html'

class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['date', 'doctor']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['date', 'doctor']

class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = '/appointments/'

class PrescriptionCreate(CreateView):
    model = Prescription
    # fields = ['name', 'size']
    form_class = PrescriptionForm
    template_name = "prescriptions/prescription_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def prescriptions_form(request):
    #     url = f'https://clinicaltables.nlm.nih.gov/api/rxterms/v3/search?terms={terms}&ef=DISPLAY_NAME,STRENGTHS_AND_FORMS'
    #     response = requests.get(url)
    #     data = response.json()

    #     context = {
    #         'prescriptionName' : data[2]['DISPLAY_NAME'][0],
    #         'prescriptionStrength': data[2]['STRENGTHS_AND_FORMS'][0][0]
    #     }

        # return render(request, 'prescriptions_form.html', context)

def add_prescription(request, user_id):

    form = PrescriptionForm(request.POST)
    
    if form.is_valid():
        new_prescription = form.save(commit=False)
        # new_prescription.name = data[2]['DISPLAY_NAME'][0]
        # new_prescription.size = data[2]['STRENGTHS_AND_FORMS'][0][0]
        new_prescription.user_id = user_id
        new_prescription.save()
    return redirect('/prescriptions', user_id=user_id)


# def provider_home(request):
#     return render (request, 'provider/index.html', {'form':SearchProvider(), 'keyword': provider_search})

def provider_search(request):
    if request.method == "POST":
        form = SearchProvider(request.POST)
    
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            response = requests.get(
            f'https://data.cms.gov/data-api/v1/dataset/862ed658-1f38-4b2f-b02b-0b359e12c78a/data?keyword={keyword}&offset=0&size=300&distinct=1').json()
            K = "Rndrng_NPI"

            memo = set()
            res = []
            for sub in response:
                if sub[K] not in memo:
                    res.append(sub)

                    memo.add(sub[K])
            
            return render(request, 'provider/index.html', {'response': res, 'form':form})
        else:   
            return HttpResponse("Form is not properly completed")
    else:
        form = SearchProvider()
    return render(request, 'provider/index.html', {'form':form})

    # print(data)
    # context = {
    #     'city' : data[0]['Rndrng_Prvdr_City'],
    #     'state' : data[0]['Rndrng_Prvdr_State_Abrvtn'],
    #     'last' : data[0]['Rndrng_Prvdr_Last_Org_Name'],
    #     'zip' : data[0]['Rndrng_Prvdr_Zip5'],
    #     'spec' : data[0]['Rndrng_Prvdr_Type']
    # }

def add_insurance(request, user_id):
    form = InsuranceForm(request.POST)
    if form.is_valid():
        new_insurance = form.save(commit=False)
        new_insurance.user_id = user_id
        new_insurance.save()
    return redirect('/insurance', user_id=user_id)

def add_file(request):
    document_file = request.FILES.get('doc-file', None)
    print(document_file, '<-- file contents')
    user_id = request.user.id
    if document_file: 
        s3 = boto3.client('s3')
        key = 'pursuitofhealth/' + uuid.uuid4().hex[:6] + document_file.name[document_file.name.rfind('.'):]
        print('File is pending')
        try: 
            s3.upload_fileobj(document_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            Document.objects.create(url=url, user_id=user_id)
        except: 
            print('An error occured uploading file to S3')
    return redirect('documents_index')
