from django.shortcuts import render
import json
import pprint
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import requests
import time
#from rest_framework import status 
#from rest_framework.response import Response
#from rest_framework.decorators import api_view
from django.http import JsonResponse 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from .models import Payment, Pnotes




# Create your views here.
#@api_view(['GET','POST',])
@csrf_exempt
def insta(request):
	return HttpResponse(status=200)

def done(request):
	if request.method == 'POST':
		b_name = request.POST.get('Name')
		b_email = request.POST.get('Email')
		b_amount = request.POST.get('Amount')
		b_purpose = request.POST.get('Purpose')
		b_mobile = request.POST.get('Mobile')
		#m_token = request.POST.get('Token')
		#m_API_KEY = request.POST.get('API')
		headers = { "X-Api-Key": 'YOUR_API_KEY', "X-Auth-Token": 'AUTH_TOKEN'}
		payload = {
			 'purpose': b_purpose,
	 		 'amount': b_amount,
	 		 'buyer_name': b_amount,
	 		 'email': b_email,
	 		 'phone': b_mobile,
			 'redirect_url': 'http://www.teamvalor.pe.hu',
	 		 'send_email': 'True',
	 		 'send_sms': 'True',
	 		 'webhook': 'http://www.example.com/webhook/',
	 		 'allow_repeated_payments': 'False',
			 }
		response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
		print response.text
		payment = Payment.objects.create(
                            name = b_name,
                            email = b_email,
                            purpose=b_purpose,
							mobile=b_mobile,
							amount=b_amount)
		return render(request,"pronote.html")
		# response2 = requests.get(
  # 					"https://www.instamojo.com/api/1.1/payment-requests/f99a76ffa2c543b2b084cba4ee6d8bde/MOJO5a06005J21512197/",
  # 					headers=headers)
		# print response2.text

def form(request):
	return render(request,'index.html')

def display(request):
	payment=Payment.objects.all().reverse()
	return render(request,'payment.html',{'payment':payment})


def note(request):
	return render(request,'note.html')

def note_done(request):
	if request.method == 'POST':
		promissory_note = request.POST.get('note_desc')
		p_days = int(request.POST.get('p-days'))
		pnotes = Pnotes.objects.create(
            pnotes = promissory_note,
            pdate = int(time.strftime("%d")) + p_days 
            )
		return render(request,"xyz.html")

def pronote(request):
	return render(request,"pronote.html")

def xyz(request):
	return render(request,"xyz.html")

def prominotes(request):
	pnotes=Pnotes.objects.all()
	return render(request,"prominotes.html",{'pnotes':pnotes})