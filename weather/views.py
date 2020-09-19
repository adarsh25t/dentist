from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')

def contact(request):

    if request.method == 'POST':
    	
    	message_name = request.POST['message-name']
    	message_email = request.POST['message-email']
    	message = request.POST['message']


    	# send an email
    	send_mail(
    		message_name, # subject
    		message, # message
    		message_email, # from email
    		['adarsh225510@gmail.com'], # to email

    		)

    	return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def pricing(request):
    return render(request, 'pricing.html')

def blog(request):
    return render(request, 'blog.html')

def bdetails(request):
    if request.method == 'POST':

        me_name = request.POST['me-name']
        me_email = request.POST['me-email']
        messages = request.POST['messages']

        return render(request, 'blog-details.html', {'me_name': me_name})


    return render(request, 'blog-details.html')

def book(request):
    
    if request.method == 'POST':

        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_day = request.POST['your-day']
        your_message = request.POST['your-message']

        return render(request, 'book.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address':your_address,
            'your_scheldule': your_scheldule, 
            'your_day': your_day,
            'your_message': your_message

            })
     
        apointment = 'Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email " Address:" + your-address + " Scheldule: " + your-scheldule + "day: " + your-day + "message: " + your-message '
        send_mail(
            message_name, # subject
            apointment, # message
            message_email, # from email
            ['adarsh225510@gmail.com'], # to email

            )

                        

    return render(request, 'book.html')