from django.db import models
from django import forms
from django.forms.models import modelformset_factory


#below you create the models that will be used to make forms in the form.py file
class Keys(models.Model):
    
    #Values in the database are the first word, second word is what the user sees
	BUILDINGS = (
		("LIB", 'Library'),
		("STRZ", 'Straz'),
		("LNTZ", 'Lentz'),		
		("JART", 'Johnson Art Center'),
		("TARC", 'TARC'),
		("CHPL", 'Chapel'),
		("DNHT", 'Denhart Hall'),
		("TARB", 'Tarble Hall'),
		("MADR", 'Madrigrano Hall'),
		("JOHN", 'Johnson Hall'),
		("SWEN", 'Swenson Hall'),
		("OAKS1", 'Oaks 1'),
		("OAKS2", 'Oaks 2'),
		("OAKS3", 'Oaks 3'),
		("OAKS4", 'Oaks 4'),
		("OAKS5", 'Oaks 5'),
		("OAKS6", 'Oaks 6'),
		)
	REASONS= (
		("NEWE", 'New Employee'),
		("NEWO", 'New Office or Facility Assignment'),
		("LOCK", 'Lock Change'),		
		("WORN", 'Worn Key Returned'),
		("OTH", 'Other (please explain)'),
		)
		
	building = models.CharField(choices=BUILDINGS, max_length=200) #The choices field uses the choices outlined above to make a select list.
	room_number = models.PositiveIntegerField(max_length=5) #'max_length' is the maximum number of characters allowed in this field
	key_code_if_known = models.CharField(max_length=100)
	issued_to = models.CharField(max_length=100)
	building1 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
	room_number1 = models.IntegerField(max_length=20000, blank=True, null=True)
	key_code_if_known1 = models.CharField(max_length=100, blank=True)
	issued_to1 = models.CharField(max_length=100, blank=True)
	building2 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
	room_number2 = models.IntegerField(max_length=20000, blank=True, null=True)
	key_code_if_known2 = models.CharField(max_length=100, blank=True)
	issued_to2 = models.CharField(max_length=100, blank=True)
	building3 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
	room_number3 = models.IntegerField(max_length=20000, blank=True, null=True)
	key_code_if_known3 = models.CharField(max_length=100, blank=True)
	issued_to3 = models.CharField(max_length=100, blank=True)
	building4 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
	room_number4 = models.IntegerField(max_length=20000, blank=True, null=True)
	key_code_if_known4 = models.CharField(max_length=100, blank=True)
	issued_to4 = models.CharField(max_length=100, blank=True)
	reason = models.CharField(choices=REASONS, max_length = 200, default = "NEWE")
	other = models.CharField(max_length = 400, blank=True)
	date_completed = models.DateField(blank=True)
	dean_sig = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=15)
	Date = models.DateField(auto_now_add=True)
	account = models.CharField(max_length=150)