import os
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import ContactForm

PROJECTS = [
    {
        "number": "01", "name": "Raku Travel", "type": "Frontend web project",
        "description": "A travel landing page presenting tour packages, destinations, testimonials and a newsletter section.",
        "stack": ["HTML", "CSS", "JavaScript"], "demo": "https://rakibul642.github.io/Travel_Project/",
        "github": "https://github.com/rakibul642", "kind": "travel",
    },
    {
        "number": "02", "name": "Architecture Landing Page", "type": "Frontend web project",
        "description": "A responsive architecture-focused landing page designed to introduce services and showcase a clean layout.",
        "stack": ["HTML", "CSS"], "demo": "https://rakibul642.github.io/ArchitectureLandingPageG3/",
        "github": "https://github.com/rakibul642", "kind": "architecture",
    },
    {
        "number": "03", "name": "Weather App", "type": "JavaScript application",
        "description": "A weather application interface that demonstrates DOM interaction and dynamic weather information.",
        "stack": ["HTML", "CSS", "JavaScript"], "demo": "https://rakibul642.github.io/WeatherApp_Project/",
        "github": "https://github.com/rakibul642", "kind": "weather",
    },
    {
        "number": "04", "name": "DOM Mini Project", "type": "JavaScript practice",
        "description": "A collection of small interactive features built to practice JavaScript and DOM manipulation.",
        "stack": ["HTML", "CSS", "JavaScript"], "demo": "https://rakibul642.github.io/DOM-mini_Project/",
        "github": "https://github.com/rakibul642", "kind": "code",
    },
    {
        "number": "05", "name": "Community Problem Reporting Platform", "type": "Collaborative full-stack project",
        "description": "A team-built platform concept that helps community members report local problems and follow their progress.",
        "stack": ["Python", "Django", "HTML", "CSS", "JavaScript"], "demo": "",
        "github": "https://github.com/israfil07/Capstone_Project", "kind": "community",
    },
]

def home(request):
    return render(request, "portfolio/home.html", {"projects": PROJECTS, "form": ContactForm()})

@require_POST
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        saved = form.save()
        if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
            try:
                send_mail(
                    subject=f"Portfolio contact: {saved.subject or 'New message'}",
                    message=f"From: {saved.name} <{saved.email}>\\n\\n{saved.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Thanks! Your message has been sent.")
            except Exception:
                messages.warning(request, "Your message was saved, but email delivery failed. I will review it from the admin panel.")
        else:
            messages.success(request, "Thanks! Your message has been saved. Email notifications are not configured yet.")
    else:
        messages.error(request, "Please check the form and try again.")
    return redirect("home")

def resume_download(request):
    path = os.path.join(settings.BASE_DIR, "media", "Rakibul-Hasan-Shuvo-Resume.pdf")
    if not os.path.exists(path):
        raise Http404("Resume file not found.")
    return FileResponse(open(path, "rb"), as_attachment=True, filename="Rakibul-Hasan-Shuvo-Resume.pdf")
