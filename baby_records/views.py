from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ToiletingForm, FeedingForm, SleepingForm, GrowthForm
from .models import Toileting, Feeding, Sleeping, Growth
from django.forms.models import model_to_dict

def index(request):
    # Get toileting and feeding recordsrecords
    latest_records_list_toilet = Toileting.objects.order_by("-toilet_time")[:5]
    latest_records_list_feed = Feeding.objects.order_by("-feed_time")[:5]
    context = {
        "latest_records_list_toilet": latest_records_list_toilet,
        "latest_records_list_feed": latest_records_list_feed,
    }
    return render(request, 'baby_records/index.html', context)

def toilet_detail(request, entry_id):
    toilet_session = ToiletingForm(data=model_to_dict(Toileting.objects.get(pk=entry_id)))
    return render(request, 'baby_records/detail.html', {'session_entry': toilet_session, 'entry_type': 'toileting'})

def feeding_detail(request, entry_id):
    feeding_session = FeedingForm(data=model_to_dict(Feeding.objects.get(pk=entry_id)))
    return render(request, 'baby_records/detail.html', {'session_entry': feeding_session, 'entry_type': 'feeding'})

def sleeping_detail(request, entry_id):
    sleeping_session = SleepingForm(data=model_to_dict(Sleeping.objects.get(pk=entry_id)))
    return render(request, 'baby_records/detail.html', {'session_entry': sleeping_session, 'entry_type': 'sleeping'})

def growth_detail(request, entry_id):
    growth_session = GrowthForm(data=model_to_dict(Growth.objects.get(pk=entry_id)))
    return render(request, 'baby_records/detail.html', {'session_entry': growth_session, 'entry_type': 'growth'})


def toilet_form(request):
    form_header = 'toileting'
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
    context = {"form": toilet_form, "form_header" : form_header, "form_url": '/baby_records/toilet_form/'}
    return render(request,'baby_records/form.html', context)


def feeding_form(request):
    form_header = 'feeding'
    if request.method == "POST": 
        feeding_form = FeedingForm(request.POST)  
        if feeding_form.is_valid(): 
            feeding_form.save() 
            try:  
                return redirect('/baby_records/feeding_form/')  
            except:  
                pass  
    else:  
        feeding_form = FeedingForm()  
    context = {"form": feeding_form, "form_header" : form_header, "form_url": '/baby_records/feeding_form/'}
    return render(request,'baby_records/form.html', context)


def sleeping_form(request):
    form_header = 'sleeping'
    if request.method == "POST": 
        sleeping_form = SleepingForm(request.POST)  
        if sleeping_form.is_valid(): 
            sleeping_form.save() 
            try:  
                return redirect('/baby_records/sleeping_form/')  
            except:  
                pass  
    else:  
        sleeping_form = SleepingForm()  
    context = {"form": sleeping_form, "form_header" : form_header, "form_url": '/baby_records/sleeping_form/'}
    return render(request,'baby_records/form.html', context)


def growth_form(request):
    form_header = 'growth measurements'
    if request.method == "POST": 
        growth_form = GrowthForm(request.POST)  
        if growth_form.is_valid(): 
            growth_form.save() 
            try:  
                return redirect('/baby_records/growth_form/')  
            except:  
                pass  
    else:  
        growth_form = GrowthForm()  
    context = {"form": growth_form, "form_header" : form_header, "form_url": '/baby_records/growth_form/'}
    return render(request,'baby_records/form.html', context)
