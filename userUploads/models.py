from django.db import models

# Create your models here.
class UserUploads(models.Model):
    Job_Description = models.TextField(blank=True, null=True)
    Resume = models.FileField(upload_to='uploads/', default='No file chosen')