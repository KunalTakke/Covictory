from django.shortcuts import render
from django.http import HttpResponse
from .models import contactform

# Create your views here.
def Dashboard(request):
    return render(request, 'Dashboard.html')

def VaccinationCenter(request):
    return render(request, 'VaccinationCenter.html')

def Statistics(request):
    return render(request, 'Statistics.html')

def ContactForm(request):
    if request.method == 'POST':
        name = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        state = request.POST.get('state')
        email = request.POST.get('email')
        mobile = request.POST.get('mob_num')
        subject = request.POST.get('subject')

        reserve = contactform(customer_name=name, mobile_number=mobile, Number_of_visitors=visitors, email_id=email,
                              transaction_id=reference, datetime=dbdatetime)
        reserve.save()


    return render(request, 'ContactForm.html')
