from django.db import models

class PDFDocument(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')  # Uploads to media/pdfs/

    def __str__(self):
        return self.name
