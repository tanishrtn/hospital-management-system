from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin', 'Administrator'
        STAFF = 'staff', 'Staff'

    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.STAFF)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    reason = models.TextField()

    class Meta:
        ordering = ['name', 'id']
        constraints = [models.CheckConstraint(condition=models.Q(age__gte=0), name='patient_age_non_negative')]

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)

    class Meta:
        ordering = ['name', 'id']
        constraints = [models.CheckConstraint(condition=models.Q(experience__gte=0), name='doctor_experience_non_negative')]

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['date', 'time', 'id']
        constraints = [
            models.UniqueConstraint(fields=['doctor', 'date', 'time'], name='unique_doctor_appointment_slot')
        ]

    def __str__(self):
        return f"{self.patient} - {self.doctor}"
