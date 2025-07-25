from django.shortcuts import render, redirect
from .models import ContactSubmission  # Make sure this model exists

def home(request):
    return render(request, 'pages/home.html')

def page1(request):
    return render(request, 'pages/page1.html')

def content(request):
    return render(request, 'pages/content.html')

def intro(request):
    return render(request, 'pages/intro.html')

def team(request):
    return render(request, 'pages/team.html')

def services(request):
    return render(request, 'pages/services.html')

def case(request):
    return render(request, 'pages/case.html')

def vision(request):
    return render(request, 'pages/vision.html')

def aims(request):
    return render(request, 'pages/aims.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'pages/contact.html', {'success': True})

    return render(request, 'pages/contact.html')


from django.shortcuts import render

def job_seekers(request):
    if request.method == "POST":
        # TODO: validate & save / email / store in DB
        pass
    return render(request, "pages/job_seekers.html")
