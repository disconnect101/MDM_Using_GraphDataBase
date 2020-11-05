from django.db import models

# Create your models here.

class Media(models.Model):
    TYPES = (
        ('PDF', 'PDF'),
        ('CSV', 'CSV'),
        ('IMG', 'Image'),
        ('TXT', 'Text'),
        ('VID', 'Video'),
        ('AUD', 'Audio'),
    )
    type = models.CharField(choices=TYPES, max_length=5)
    name = models.CharField(max_length=200)
    media = models.FileField(upload_to='')

