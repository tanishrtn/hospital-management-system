# Hospital Management System

A Django web application for managing hospital workflows, including user accounts, patient records, doctor information, and appointments.

## Tech stack

- Python
- Django 6
- SQLite (development)
- HTML/CSS

## Features

- User registration and login
- Patient record management
- Doctor management
- Appointment scheduling
- Dashboard for hospital operations

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

On Windows PowerShell, activate the environment with `.venv\\Scripts\\Activate.ps1`.

## Security note

Set `DJANGO_SECRET_KEY` to a unique, private value before deployment. The included settings are for local development only.
