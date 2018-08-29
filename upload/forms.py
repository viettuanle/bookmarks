from django import forms
from upload.models import Document, MyModel, Images


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class DocumentForm2(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('document', )

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=Images
        fields=('path',)