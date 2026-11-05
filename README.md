# Rakibul Hasan Shuvo — Developer Portfolio

A responsive Django-powered portfolio for a Python/Django full-stack developer.

## Features
- Responsive home, about, skills, projects, education, blog and contact sections
- Dark/light theme toggle (saved in browser)
- Animated section reveals and mobile navigation
- Resume download served by Django
- Contact form with server-side validation and database storage
- Optional email notification through SMTP
- Django admin for reviewing contact messages

## Run locally
1. Install Python 3.10+.
2. Create and activate a virtual environment:
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and set a secure `SECRET_KEY`.
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
7. Open `http://127.0.0.1:8000`

## Admin
Create an admin user with `python manage.py createsuperuser`, then visit `/admin/`.

## Email setup
The contact form always stores valid messages in the database. To send email notifications, configure the SMTP values in `.env`. For Gmail, use an App Password (not your normal account password).

## Deploy
For a production deployment:
- Set `DEBUG=False` and a strong `SECRET_KEY`.
- Set `ALLOWED_HOSTS` to your domain.
- Configure a production database (PostgreSQL recommended).
- Run `python manage.py collectstatic`.
- Use a platform that supports Django (for example Render, Railway, or a VPS) with Gunicorn.
- Configure HTTPS and SMTP credentials as environment variables.
- Never commit `.env`, database credentials, or email passwords.

## Content to personalize
Review the project descriptions and education details in `portfolio/views.py` before publishing. Add verified dates, project repository links, and any missing live demos when available.
