from django import forms
from django.forms import ModelForm
from .models import * 

# building a form for the Task model

# a good naming convention for form classis 'model name + Form'
class TaskForm(forms.ModelForm):

	class Meta:
		model = Task # model for which we're building the form 
		fields = "__all__" # include all fields of the model in the form


