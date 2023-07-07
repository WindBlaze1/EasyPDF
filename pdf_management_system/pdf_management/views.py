from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def pdf_read(request, filepath='C:\\Users\\harit\\Documents\\Project\\PDF System\\pdf_management_system\\static\\pdf.pdf', filename='pdf1.pdf'):
    with open(filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = f'filename={filename}'
    # return response
    return render(request,'PDF.html',{'pdf_file':response})
    
