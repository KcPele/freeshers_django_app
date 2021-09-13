from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import UploadFile, SubscribedEmail
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.contrib import messages

def home(request):
	return render(request, 'pdf/base.html')


def search_view(request):
    query = request.GET.get('query')
    
    qs = UploadFile.objects.search(query=query)
    context = {
        "object_list":qs,
    }
   
    return render(request, 'pdf/search.html', context)



class ListUploadFile(ListView):
	paginate_by = 4
	model = UploadFile



def email_contact(request):
	if request.method == 'Get':
		return redirect('home')
	else:
		name_email = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message_email = request.POST['message_email']
		message_email2 = f'{message_email} from {email}'
		try:
			send_mail(subject, message_email2, email, 
			[settings.EMAIL_HOST_USER], fail_silently=False,)
			messages.success(request, 'Thanks, A response has been sent to your mail')
			return redirect('home')
			
		except:
			messages.error(request, 'Email not sent, Something went wrong. Try again!')
			return redirect('home')
		



def email_subscribe(request):
	
	if request.method == 'POST':
		message_email = 'Thank u for subscribing, You will be notified once there is a new material'
		subject = 'Pdf Subscription'
		subscribe_email = request.POST['email_subscribe']
		SubscribedEmail.objects.create(email_name=subscribe_email)
		send_mail(subject, message_email, settings.EMAIL_HOST_USER, 
			[subscribe_email], fail_silently=False,)
		messages.success(request, 'Thank you for subscribing, Check your mail or spam box')
		return redirect('/')

	else:
		return redirect('home')