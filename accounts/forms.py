from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient, Doctor, Appointment


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']


class PatientForm(forms.ModelForm):
    def clean_age(self):
        age = self.cleaned_data['age']
        if not 0 <= age <= 130:
            raise forms.ValidationError('Enter an age between 0 and 130.')
        return age

    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact', 'reason']


class DoctorForm(forms.ModelForm):
    def clean_experience(self):
        experience = self.cleaned_data['experience']
        if not 0 <= experience <= 80:
            raise forms.ValidationError('Enter experience between 0 and 80 years.')
        return experience

    class Meta:
        model = Doctor
        fields = ['name', 'department', 'specialization', 'qualification', 'experience']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
