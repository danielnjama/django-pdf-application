from django.shortcuts import render
from django.conf import settings
from .models import PDFDocument

def pdf_list(request):
    pdfs = PDFDocument.objects.all()
    # for pdf in pdfs:
    #     pdf.absolute_url = request.build_absolute_uri(pdf.file.url)  # Convert to full URL
    return render(request, 'index.html', {'pdfs': pdfs})
