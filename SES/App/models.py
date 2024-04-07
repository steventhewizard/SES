from django.db import models

# Create your models here.
class rubric (models.Model) :
   name=models.CharField(max_length=50) 
   pdf_file = models.FileField(upload_to='pdfs/')

class Essay(models.Model) :
   pdf_file = models.FileField(upload_to='essays/')
   