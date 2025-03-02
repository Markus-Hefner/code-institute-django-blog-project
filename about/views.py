from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        print("Received a POST request")
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            print(collaborate_form)

            # collaborate_request = collaborate_form.save(commit=False)
            # collaborate_request.name = collaborate_form.name
            # collaborate_request.email = collaborate_form.email
            # collaborate_request.message = collaborate_form.message
            # collaborate_request.read = collaborate_form.read
            # collaborate_request.save
            collaborate_form.save
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form,
         },
    )
