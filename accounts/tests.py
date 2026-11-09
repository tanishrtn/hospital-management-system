from datetime import date, time

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .forms import PatientForm
from .models import Appointment, Doctor, Patient


class AuthenticationTests(TestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('dashboard')}")

    def test_authenticated_user_can_open_dashboard(self):
        user = get_user_model().objects.create_user(username='staff', password='safe-test-password')
        self.client.force_login(user)
        self.assertEqual(self.client.get(reverse('dashboard')).status_code, 200)


class RecordWorkflowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='staff', password='safe-test-password')
        self.client.force_login(self.user)
        self.patient = Patient.objects.create(name='Asha', age=28, gender='Female', contact='9999999999', reason='Checkup')
        self.doctor = Doctor.objects.create(name='Dr Rao', department='Medicine', specialization='General', qualification='MBBS', experience=7)

    def test_patient_age_validation(self):
        form = PatientForm(data={'name': 'Invalid', 'age': -1, 'gender': 'Other', 'contact': '1', 'reason': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)

    def test_delete_requires_post(self):
        response = self.client.get(reverse('delete_patient', args=[self.patient.id]))
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Patient.objects.filter(id=self.patient.id).exists())

    def test_duplicate_doctor_slot_is_rejected(self):
        slot = {'patient': self.patient, 'doctor': self.doctor, 'date': date(2027, 1, 10), 'time': time(10, 30)}
        Appointment.objects.create(**slot)
        with self.assertRaises(IntegrityError), transaction.atomic():
            Appointment.objects.create(**slot)
