from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render, redirect
from bookmarks.forms import EmailForm
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


def home(request):
    template_name = "home.html"
    return render(request,template_name=template_name)

def sendemail(request):

    form = EmailForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_fullname = form.cleaned_data.get("fullname")
        subject = 'Test sending email, Django project'
        from_email = settings.EMAIL_HOST_USER
        contact_message = """You got message from %s
        Name: %s
        with message: %s 
        Note: This is auto email, send from %s
        """%(form_email,form_fullname,form_message,from_email)

        if form_message:
            print(form_message)
        if subject and form_message and from_email:
            try:
                send_mail(subject, contact_message, from_email, ['vietle.tuan@gmail.com','saomaicodon10@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
    context = {'form':form}
    return render(request,'formemail.html',context)