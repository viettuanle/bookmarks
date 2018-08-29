from django.db import models
from django.conf    import settings
user = settings.AUTH_USER_MODEL
# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.document

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)

class MyModel(models.Model):
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, default="")
    def __str__(self):
        return self.document

class Images(models.Model):
    path = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.path
class Post(models.Model):
    title = models.CharField(max_length=120,null=True,blank=True)
    image = models.ForeignKey(Images,on_delete=models.CASCADE,related_name='image_pose')
    def __str__(self):
        return "%s, image: %s" %(self.title,self.image)