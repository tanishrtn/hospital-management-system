from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
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
        messages.error(request, 'Invalid username or password.')

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
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {
        'patients': Patient.objects.count(),
        'doctors': Doctor.objects.count(),
        'appointments': Appointment.objects.count(),
        'recent_patients': Patient.objects.all()[:5],
        'doctors_list': Doctor.objects.all()[:5],
    })


# PATIENTS
@login_required
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


@login_required
@require_POST
def delete_patient(request, id):
    get_object_or_404(Patient, id=id).delete()
    return redirect('patients')


# DOCTORS
@login_required
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


@login_required
@require_POST
def delete_doctor(request, id):
    get_object_or_404(Doctor, id=id).delete()
    return redirect('doctors')


# APPOINTMENTS
@login_required
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


@login_required
@require_POST
def delete_appointment(request, id):
    get_object_or_404(Appointment, id=id).delete()
    return redirect('appointments')
