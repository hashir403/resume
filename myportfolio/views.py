# hashir
# hashir403!

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from django.shortcuts import render, get_object_or_404

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        email_title = request.POST.get("email_title")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            email_title=email_title,
            message=message,
        )
        # Email content
        subject = f"New Contact Form Submission: {email_title}"
        body = f"""
        You received a new message from your website:

        Name: {name}
        Email: {email}
        Number: {number}

        Subject: {email_title}

        Message:
        {message}
        """

        # Send email
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,   # from
            ["projecttest09python@gmail.com"],  # to
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("index")
         
    return render(request, "index.html")


def project(request):
    return render(request, 'project.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, "project.html", {"projects": projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_detail.html", {"project": project})