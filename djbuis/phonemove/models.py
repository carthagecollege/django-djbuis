from django.db import models
from django import forms
from django.forms.models import modelformset_factory

class Phone(models.Model):

	REASONS= (
		("MOVE", 'Move'),
		("ADD", 'Add'),
		("REPL", 'Replacement'),		
		("CHNG", 'Change of Service'),
		)
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=200)
	user_number = models.CharField(max_length=15)
	request = models.CharField(choices=REASONS, max_length=100, default="MOVE")
	from_location = models.CharField(max_length=500)
	to_location = models.CharField(max_length=500)
	caller_id = models.CharField(max_length=500)
	date_of_change = models.DateField()
	email = models.BooleanField()
