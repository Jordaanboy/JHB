from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
#from django.conf import settings

def home(request):
	return render(request,'home.html',{})

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		
		data = {
				'name': name,
				'email': email,
				'subject': subject,
				'message': message
		}
		message = '''
		New message: {}

		From: {}
		'''.format(data['message'],data['email'])
		send_mail(data['subject'], message,'',['karimjordan79@gmail.com'])
		return render(request,'contact.html',{'P_name' : P_name})
	return render(request,'contact.html',{})

def about(request):
	return render(request,'about.html',{})

def service(request):
	return render(request,'service.html',{})

def price(request):
	return render(request,'price.html',{})

def appointment(request):
	return render(request,'appointment.html',{})
# Create your views here.