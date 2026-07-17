from .models import Patient, Doctor, Appointment
import random
from datetime import date, time


def run():

    Patient.objects.all().delete()
    Doctor.objects.all().delete()
    Appointment.objects.all().delete()

    doctor_data = [
        ("Dr. Arjun Mehta", "Cardiology"),
        ("Dr. Riya Sharma", "Neurology"),
        ("Dr. Kunal Verma", "Orthopedics"),
        ("Dr. Sneha Kapoor", "Dermatology"),
        ("Dr. Rahul Nair", "ENT"),
        ("Dr. Ananya Iyer", "Gynecology"),
        ("Dr. Vikram Singh", "General Medicine"),
        ("Dr. Neha Gupta", "Pediatrics"),
        ("Dr. Aman Khanna", "Oncology"),
        ("Dr. Priya Joshi", "Psychiatry"),
    ]

    doctors = []
    for name, dept in doctor_data:
        d = Doctor.objects.create(
            name=name,
            department=dept,
            specialization=dept,
            qualification="MBBS, MD",
            experience=random.randint(3, 20),
        )
        doctors.append(d)

    patient_names = [
        "Rahul Verma", "Aman Singh", "Neha Sharma", "Priya Kapoor",
        "Rohan Mehta", "Anjali Gupta", "Vikas Nair", "Sneha Iyer",
        "Karan Malhotra", "Simran Kaur"
    ]

    patients = []
    for name in patient_names:
        p = Patient.objects.create(
            name=name,
            age=random.randint(20, 60),
            gender=random.choice(["Male", "Female"]),
            contact="9876543210",
            reason=random.choice(["Fever", "Injury", "Checkup", "Headache"]),
        )
        patients.append(p)

    for i in range(10):
        Appointment.objects.create(
            patient=random.choice(patients),
            doctor=random.choice(doctors),
            date=date.today(),
            time=time(hour=random.randint(9, 17)),
        )

    print(" Clean professional data inserted")