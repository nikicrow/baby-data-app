from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Toileting, Feeding


def index(request):
    latest_records_list_t = Toileting.objects.order_by("-toilet_time")[:10]
    # toilet_output = ", ".join([q.toilet_time.strftime("%m/%d/%Y-%H:%M:%S") for q in latest_records_list_t])
    template = loader.get_template("baby_records/index.html")
    context = {
        "latest_records_list_t": latest_records_list_t,
    }
    # latest_records_list_f = Feeding.objects.order_by("-feed_time")[:10]
    # feed_output = ", ".join([q.feed_time.strftime("%m/%d/%Y-%H:%M:%S") for q in latest_records_list_f])
    return HttpResponse(template.render(context, request))

def detail(request, entry_id):
    return HttpResponse("You're looking at entry %s." % entry_id)

def toilet_record(request, entry_id):
    toilet_entry = get_object_or_404(Toileting, pk=entry_id)
    return HttpResponse("You're looking at entry %s." % toilet_entry) #HttpResponseRedirect(reverse("baby_app:results", args=(toilet_entry.id,)))

def toilet_results(request, entry_id):
    toilet_entry = get_object_or_404(Toileting, pk=entry_id)
    return render(request, "baby_records/results.html", {"entry": toilet_entry})