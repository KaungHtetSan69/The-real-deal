from django.shortcuts import render
from django.core.mail import send_mail
def index(request):
    return render(request, 'index.html',{})
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name': message_name})
        send_mail(
            message_name,
            message,
            message_email,
            ['citydentalmm.21@gmail.com']


        )

    else:
        return render(request, 'contact.html', {})
def about(request):
    return render(request, 'about.html',{})
def gallery(request):
    return render(request, 'gallery.html',{})
def services(request):
    return render(request, 'services.html',{})
