from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Toileting, Feeding


def index(request):
    # Get toileting and feeding recordsrecords
    latest_records_list_toilet = Toileting.objects.order_by("-toilet_time")[:10]
    latest_records_list_feed = Feeding.objects.order_by("-feed_time")[:10]
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
    return HttpResponse("You're looking at toilet entry %s." % toilet_entry) #HttpResponseRedirect(reverse("baby_app:results", args=(toilet_entry.id,)))
