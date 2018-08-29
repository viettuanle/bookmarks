from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from upload.forms import DocumentForm, DocumentForm2, ImageUploadForm
from upload.models import Images


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
    })


def user_upload(request):
    if request.method == 'POST':
        form = DocumentForm2(request.POST, request.FILES)
        if form.is_valid():
            mymodel = form.save(commit=False)
            mymodel.user = request.user
            mymodel.save()
            return redirect('home')
    else:
        form = DocumentForm2()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
    })

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'upload/image_form_upload.html', {'form': form})
def display_image(request):
    all_images = Images.objects.all()
    return render(request,'upload/display_images.html',{'all_images':all_images})