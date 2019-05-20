from django.shortcuts import render
import xlrd
from django.http import HttpResponseRedirect
from . models import WorkFile
from django.urls import reverse

def home(request):

    if request.method == 'POST':
        workfile1 = WorkFile()
        workfile1.file = request.FILES['myfile']
        file1 = workfile1.file
        workfile1.save()
        return HttpResponseRedirect(reverse('chatte',))
    else:
        return render(request, 'read/home.html')