from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, PatientForm, DoctorForm, AppointmentForm
from .models import Patient, Doctor, Appointment


# ✅ REQUIRED (THIS FIXES YOUR ERROR)
def home_view(request):
    return redirect('login')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')


# REGISTER
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# DASHBOARD
def dashboard(request):
    return render(request, 'dashboard.html', {
        'patients': Patient.objects.count(),
        'doctors': Doctor.objects.count(),
        'appointments': Appointment.objects.count(),
        'recent_patients': Patient.objects.all()[:5],
        'doctors_list': Doctor.objects.all()[:5],
    })


# PATIENTS
def patients_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()

    patients = Patient.objects.all()

    return render(request, 'accounts/patients.html', {
        'form': form,
        'patients': patients
    })


def delete_patient(request, id):
    Patient.objects.get(id=id).delete()
    return redirect('patients')


# DOCTORS
def doctors_view(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()

    doctors = Doctor.objects.all()

    return render(request, 'accounts/doctors.html', {
        'form': form,
        'doctors': doctors
    })


def delete_doctor(request, id):
    Doctor.objects.get(id=id).delete()
    return redirect('doctors')


# APPOINTMENTS
def appointments_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()

    appointments = Appointment.objects.all()

    return render(request, 'accounts/appointments.html', {
        'form': form,
        'appointments': appointments
    })


def delete_appointment(request, id):
    Appointment.objects.get(id=id).delete()
    return redirect('appointments')