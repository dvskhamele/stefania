from django.shortcuts import render
import xlrd
from django.http import HttpResponseRedirect
from . models import WorkFile
from django.urls import reverse
from rest_framework.generics import get_object_or_404
from rest_framework import generics , status
from read.serializers import *
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from example_app.views import *

def home(request):
	if request.method == 'POST':
		workfile1 = WorkFile()
		workfile1.file = request.FILES['myfile']
		file1 = workfile1.file
		workfile1.save()
		return HttpResponseRedirect(reverse('chatte',))
	else:
		return render(request, 'read/home.html')

class SendData(generics.ListCreateAPIView):

	serializer_class = DataSerializer
	authentication_classes = (TokenAuthentication,)
	def post(self, request, format='json'):
		serializer = DataSerializer(data=request.data)
		if serializer.is_valid():
			lst = []
			inst = serializer.save()
			# inst.data = inst.data			
			inst.mess = inst.mess
			inst.data1 = inst.data
			# sendit(inst.data1, inst.mess)
			try:
				sendit(inst.data1, inst.mess)
			except:
				return HttpResponseRedirect(redirect_to='/static/img/screenie.png')
				# return HttpResponse('example_app/static/img/screenie.png', content_type="image/png")
			# return HttpResponseRedirect(reverse('chatte',))
		else:
			return Response({"Status": "error"})

	def get_queryset(self):
		return WorkFile.objects.all()  
