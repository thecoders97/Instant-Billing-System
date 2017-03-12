from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import time
# Create your models here.
class Payment(models.Model):
	name=models.CharField(max_length=100,null=True)
	purpose=models.TextField(null=True)
	email=models.CharField(max_length=100)
	mobile=models.IntegerField()
	amount=models.IntegerField()
	date=models.DateTimeField(auto_now=True)
	paymentid=models.CharField(max_length=100,null=True)
	status=models.CharField(max_length=100,null=True)
	created_at=models.CharField(max_length=100,null=True)
	modified_at=models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.name

class Pnotes(models.Model):
	pnotes = models.TextField(null=True)
	pdate = models.IntegerField(null=True)

	def __str__(self):
		return self.pnotes