from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ToiletingForm, BreastFeedingForm, BottleFeedingForm, SleepingForm, GrowthForm
from .models import Toileting, BreastFeeding, BottleFeeding, Sleeping, Growth
from django.forms.models import model_to_dict

def index(request):
    context = {}
    return render(request, 'baby_records/index.html', context)


def toilet_main_page(request):
    # Show toileting main things
    latest_records_list = Toileting.objects.order_by("-toilet_time")[:10]
    context = {
        "latest_records_list": latest_records_list,
        "entry_type": 'toileting',
    }
    return render(request, 'baby_records/main_toilet.html', context)


def feed_main_page(request):
    # Show feed main things
    latest_records_list_br = BreastFeeding.objects.order_by("-feed_time")[:10]
    latest_records_list_bt = BottleFeeding.objects.order_by("-feed_time")[:10]
    context = {
        "latest_records_list_br": latest_records_list_br,
        "latest_records_list_bt": latest_records_list_bt,
        "entry_type": 'feeding',
    }
    return render(request, 'baby_records/main_feed.html', context)


def sleep_main_page(request):
    # Show feed main things
    latest_records_list = Sleeping.objects.order_by("-nap_start_time")[:10]
    context = {
        "latest_records_list": latest_records_list,
        "entry_type": 'sleeping',
    }
    return render(request, 'baby_records/main_sleep.html', context)


def growth_main_page(request):
    # Show feed main things
    latest_records_list = Growth.objects.order_by("-measurement_time")[:10]
    context = {
        "latest_records_list": latest_records_list,
        "entry_type": 'growth',
    }
    return render(request, 'baby_records/main_growth.html', context)

### CREATE

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


def breast_feeding_form(request):
    form_header = 'breast feeding'
    if request.method == "POST": 
        feeding_form = BreastFeedingForm(request.POST)  
        if feeding_form.is_valid(): 
            feeding_form.save() 
            try:  
                return redirect('/baby_records/breast_feeding_form/')  
            except:  
                pass  
    else:  
        feeding_form = BreastFeedingForm()  
    context = {"form": feeding_form, "form_header" : form_header, "form_url": '/baby_records/breast_feeding_form/'}
    return render(request,'baby_records/form.html', context)


def bottle_feeding_form(request):
    form_header = 'bottle feeding'
    if request.method == "POST": 
        feeding_form = BottleFeedingForm(request.POST)  
        if feeding_form.is_valid(): 
            feeding_form.save() 
            try:  
                return redirect('/baby_records/bottle_feeding_form/')  
            except:  
                pass  
    else:  
        feeding_form = BottleFeedingForm()  
    context = {"form": feeding_form, "form_header" : form_header, "form_url": '/baby_records/bottle_feeding_form/'}
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

### READ

def toilet_detail(request, entry_id):
    form_header = 'toileting'
    toilet_session = ToiletingForm(data=model_to_dict(Toileting.objects.get(pk=entry_id)))
    context = {'session_entry': toilet_session, 'entry_type': 'toilet', 'form_header': form_header}
    return render(request, 'baby_records/detail.html', context)

def breast_feeding_detail(request, entry_id):
    form_header = 'breast feeding'
    feeding_session = BreastFeedingForm(data=model_to_dict(BreastFeeding.objects.get(pk=entry_id)))
    context = {'session_entry': feeding_session, 'entry_type': 'breast feeding', 'form_header': form_header}
    return render(request, 'baby_records/detail.html', context)

def bottle_feeding_detail(request, entry_id):
    form_header = 'bottle feeding'
    feeding_session = BottleFeedingForm(data=model_to_dict(BottleFeeding.objects.get(pk=entry_id)))
    context = {'session_entry': feeding_session, 'entry_type': 'bottle feeding', 'form_header': form_header}
    return render(request, 'baby_records/detail.html', context)

def sleeping_detail(request, entry_id):
    form_header = 'sleeping'
    sleeping_session = SleepingForm(data=model_to_dict(Sleeping.objects.get(pk=entry_id)))
    context = {'session_entry': sleeping_session, 'entry_type': 'sleeping', 'form_header': form_header}
    return render(request, 'baby_records/detail.html', context)

def growth_detail(request, entry_id):
    form_header = 'growth measurements'
    growth_session = GrowthForm(data=model_to_dict(Growth.objects.get(pk=entry_id)))
    context = {'session_entry': growth_session, 'entry_type': 'growth', 'form_header': form_header}
    return render(request, 'baby_records/detail.html', context)

### UPDATE

def toilet_update(request, entry_id):
    form_header = 'toileting'
    record = Toileting.objects.get(pk = entry_id)
    form = ToiletingForm(request.POST or None, instance=record)  
    if form.is_valid():
        form.save()
        return redirect('/baby_records/')
    context = {'session_entry': record, 'entry_type': 'toileting', 'form': form, 'form_header': form_header}
    return render(request,'baby_records/update_record.html', context ) #redirect('/baby_records/') #HttpResponse('Record updated') # 

def breast_feed_update(request, entry_id):
    form_header = 'breast feeding'
    record = BreastFeeding.objects.get(pk = entry_id)
    form = BreastFeedingForm(request.POST or None, instance=record)  
    if form.is_valid():
        form.save()
        return redirect('/baby_records/')
    context = {'session_entry': record, 'entry_type': 'breast feeding', 'form': form, 'form_header': form_header}
    return render(request,'baby_records/update_record.html', context ) #redirect('/baby_records/') #HttpResponse('Record updated') # 

def bottle_feed_update(request, entry_id):
    form_header = 'bottle feeding'
    record = BottleFeeding.objects.get(pk = entry_id)
    form = BottleFeedingForm(request.POST or None, instance=record)  
    if form.is_valid():
        form.save()
        return redirect('/baby_records/')
    context = {'session_entry': record, 'entry_type': 'bottle feeding', 'form': form, 'form_header': form_header}
    return render(request,'baby_records/update_record.html', context ) #redirect('/baby_records/') #HttpResponse('Record updated') # 


def sleep_update(request, entry_id):
    form_header = 'sleeping'
    record = Sleeping.objects.get(pk = entry_id)
    form = SleepingForm(request.POST or None, instance=record)  
    if form.is_valid():
        form.save()
        return redirect('/baby_records/')
    context = {'session_entry': record, 'entry_type': 'sleeping', 'form': form, 'form_header': form_header}
    return render(request,'baby_records/update_record.html', context ) #redirect('/baby_records/') #HttpResponse('Record updated') # 

def growth_update(request, entry_id):
    form_header = 'growth measurements'
    record = Growth.objects.get(pk = entry_id)
    form = GrowthForm(request.POST or None, instance=record)  
    if form.is_valid():
        form.save()
        return redirect('/baby_records/')
    context = {'session_entry': record, 'entry_type': 'growth', 'form': form, 'form_header': form_header}
    return render(request,'baby_records/update_record.html', context ) #redirect('/baby_records/') #HttpResponse('Record updated') # 

### DELETE

def toilet_delete(request, entry_id):
   record = Toileting.objects.get(pk = entry_id)
   record.delete()
   return redirect('/baby_records/main_toilet')

def breast_feed_delete(request, entry_id):
   record = BreastFeeding.objects.get(pk = entry_id)
   record.delete()
   return redirect('/baby_records/main_feed')

def bottle_feed_delete(request, entry_id):
   record = BottleFeeding.objects.get(pk = entry_id)
   record.delete()
   return redirect('/baby_records/main_feed')

def sleep_delete(request, entry_id):
   record = Sleeping.objects.get(pk = entry_id)
   record.delete()
   return redirect('/baby_records/main_sleep')

def growth_delete(request, entry_id):
   record = Growth.objects.get(pk = entry_id)
   record.delete()
   return redirect('/baby_records/main_growth')
