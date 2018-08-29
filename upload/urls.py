from django.conf.urls import url

from bookmarks.views import sendemail
from upload.views import simple_upload, model_form_upload, user_upload, upload_image, \
    display_image

app_name = "upload"
urlpatterns = [

    url(r'^simple/$', simple_upload, name='simple_upload'),
    url(r'^modelupload/$', model_form_upload, name='model_upload'),
    url(r'^userupload/$', user_upload, name='user_upload'),
    url(r'^imageupload/$', upload_image, name='image_upload'),
    url(r'^displayimage/$', display_image, name='display_image'),

]
