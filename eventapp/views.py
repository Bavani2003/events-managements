from django.shortcuts import render,redirect
from . models import Decoration
from . models import Catering
from . models import Photoshoot
from . forms import BookingForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def decoration(request):
    dict_dec={
        'dec':Decoration.objects.all()
    }
    amount=request.POST.get('amount','')
    return render(request,'decoration.html', dict_dec)

def catering(request):

    dict_cat={
        'cat':  Catering.objects.all()
    }
    amount=request.POST.get('amount','')
    return render(request,'catering.html',dict_cat)
def photoshoot(request):
    dict_ph={
        'ph': Photoshoot.objects.all()
    }
    amount=request.POST.get('amount','')
    return render(request,'photoshoot.html',dict_ph)
def booking(request):
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():

            booking.save()

            messages.info(request, 'Successfully booked! Thank you.')

            # Redirect to a different page or display a different template if needed
            return redirect('/')  # Replace 'home' with the appropriate URL name


    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

