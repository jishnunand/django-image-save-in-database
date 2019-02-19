from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
DEFAULT = '--'
MALE = 'MALE'
FEMALE = 'FEMALE'
GENDER = (
	(DEFAULT, '--'),
	(MALE, 'MALE'),
	(FEMALE, 'FEMALE')
	)

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	employee_image = models.BinaryField(blank=True)
	# image_link = models.CharField(max_length=30)
	employee_phone = models.CharField(max_length=10)
	employee_address = models.TextField()
	employee_gender = models.CharField(max_length=6, choices=GENDER, default=DEFAULT)