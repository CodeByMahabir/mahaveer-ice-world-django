# home/views.py
from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.urls import reverse

# Index view
def index(request):
    context = {
        "variable1": "Mahaveer is great",
        "variable2": "Rohan is great"
    }
    return render(request, 'index.html', context)

# About view
def about(request):
    return render(request, 'about.html')

# Services view
def services(request):
    return render(request, 'services.html')

# Contact view
def contact(request):
    if request.method == "POST":
        # Handling form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, description=description, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

        # Redirecting to avoid form resubmission
        return HttpResponseRedirect(reverse('contact'))

    # Handling GET request
    return render(request, 'contact.html')
