from rest_framework import serializers
from .models import *
# from rest_framework.validators import UniqueValidator
# from datetime import datetime
from django import forms
import random
# from django_countries.fields import CountryField

class DataSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkFile
		fields = '__all__'