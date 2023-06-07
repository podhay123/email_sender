from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method == "POST":
        message = request.POST["message"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        send_mail(
        subject,
        message,
        "settings.EMAIL_HOST_USER",
        [email],
        fail_silently=False,
        )
    return render(request, "core/index.html")