from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ToiletingForm
from .models import Toileting, Feeding


def index(request):
    # Get toileting and feeding recordsrecords
    latest_records_list_toilet = Toileting.objects.order_by("-toilet_time")[:5]
    latest_records_list_feed = Feeding.objects.order_by("-feed_time")[:5]
    context = {
        "latest_records_list_toilet": latest_records_list_toilet,
        "latest_records_list_feed": latest_records_list_feed,
    }
    return render(request, 'baby_records/index.html', context)

def detail(request, entry_id):
    toilet_session = Toileting.objects.get(pk=entry_id)
    return render(request, 'baby_records/detail.html', {'entry': toilet_session})

def toilet_record(request, entry_id):
    toilet_entry = get_object_or_404(Toileting, pk=entry_id)
    return HttpResponse("You're looking at toilet entry %s." % toilet_entry) 
    #HttpResponseRedirect(reverse("baby_app:results", args=(toilet_entry.id,)))

def toilet_form(request):
    if request.method == "POST": 
        toilet_form = ToiletingForm(request.POST)  
        if toilet_form.is_valid(): 
            toilet_form.save() 
            try:  
                return redirect('/baby_records/toilet_form/')  
            except:  
                pass  
    else:  
        toilet_form = ToiletingForm()  
    return render(request,'baby_records/form.html', {"toilet_form": toilet_form})
