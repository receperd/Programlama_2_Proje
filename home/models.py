from django.db import models


# Create your models here.
class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    smtpserver = models.CharField(max_length=20)
    smtpemail = models.CharField(max_length=20)
    smtppassword = models.CharField(max_length=20)
    smtpport = models.CharField(max_length=20)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    aboutus = models.CharField(max_length=50)
    contact = models.TextField()
    references = models.TextField()

    def __str__(self):
        return self.title
