# NoctraCare Hospital Operations

A tested Django application for managing authenticated hospital workflows: patient records, doctors, appointment slots, and operational dashboard metrics.

## What works

- Account registration, login, logout, and protected application routes
- Patient and doctor creation with server-side validation
- Appointment scheduling with duplicate doctor-slot protection
- POST-only record deletion with CSRF protection
- Dashboard totals and recent records
- SQLite persistence for local development
- Docker-based startup and GitHub Actions verification

## Architecture

```text
Browser -> Django views/forms -> ORM -> SQLite
             |                   |
             +-- authentication  +-- patients, doctors, appointments
```

## Run locally

Requires Python 3.12+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000>, register a staff account, and use the dashboard.

## Run with Docker

```bash
docker compose up --build
```

The application is available at <http://127.0.0.1:8000>. The named volume preserves the development database.

## Verify

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

The automated tests cover access control, form validation, safe deletion, dashboard access, and appointment collision protection.

## Repository map

```text
accounts/                 Domain models, forms, views, templates, tests
core/                     Django settings and URL configuration
static/                   Application styling and images
.github/workflows/ci.yml  Automated checks
Dockerfile                Reproducible Python runtime
docker-compose.yml        One-command local stack
```

## Security and deployment

The included configuration is for demonstration and development. Before handling real patient information, use managed secrets, HTTPS, role-specific authorization, encrypted production storage, audit logging, backups, retention controls, and an institutional privacy review. Never commit a real `DJANGO_SECRET_KEY` or patient data.
