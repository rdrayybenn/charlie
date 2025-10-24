# Ride - Ride Booking Platform (Django)

This repository contains a Django-based ride booking platform with three main apps: `accounts`, `rides`, and `dashboard`.

Features implemented (skeleton):
- Custom user model (`accounts.CustomUser`) with fields first_name, middle_name, last_name, user_role, balance.
- Ride and RideEvent models in `rides` app.
- Views and templates scaffolded for signup/signin/profile, ride create/list/detail, and staff dashboard placeholders.
- Template inheritance with `base.html` and local Bootstrap served from `static/` (no CDN).
- `django-storages` placeholders and instructions to host static files on AWS S3.

Quick start (local):

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Set Django secret key and configure env vars (for local development you can set DEBUG=True in settings but recommended to use env vars):

Create a `.env` file or set environment variables:

```
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_STORAGE_BUCKET_NAME=your-bucket
```

3. Run migrations and start server:

```powershell
python manage.py migrate
python manage.py runserver
```

4. Create a superuser:

```powershell
python manage.py createsuperuser
```

Deployment notes:
- This README includes guidance to deploy to Heroku, Render, Railway, or similar providers. For AWS S3 static hosting, configure `django-storages` with boto3 and set `STATICFILES_STORAGE` to use S3Boto3Storage. See `ride_project/settings.py` for placeholders.

What remains / next steps:
- Implement full UI flows and validations as required by the assignment (this scaffold provides a working foundation).
- Add tests, CI, and final deployment steps.

See the repository files for implementation details.
