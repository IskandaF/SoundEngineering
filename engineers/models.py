from django.db import models
class Engineer(models.Model):
    ENGLISH="eng"
    FRENCH="fr"
    RUSSIAN="ru"

    LANGUAGE=[((ENGLISH),("English")),((FRENCH),("Française")),((RUSSIAN),("Русский"))]
    firstname=models.CharField(max_length=32)
    lastname=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    vkid=models.CharField(max_length=32)
    language=models.CharField(choices=LANGUAGE,max_length=32,default=RUSSIAN)
# Create your models here.
