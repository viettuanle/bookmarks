from django.contrib import admin
from upload.models import Document, MyModel
# Register your models here.
admin.site.register(MyModel)
admin.site.register(Document)
