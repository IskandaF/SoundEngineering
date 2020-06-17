from django.db import models
from users.forms import User
from django.contrib.auth.models import User
from engineers.models import Engineer

def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class Project(models.Model):
    name=models.CharField("Name of the project",max_length=200)
    engineer=models.ForeignKey(Engineer,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    uploadfile=models.FileField(upload_to=user_directory_path)
    def __str__(self):
        return (self.name)


class Track(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,verbose_name="Name of the track")
    def __str__(self):
        return (self.name)


    
# Create your models here.
