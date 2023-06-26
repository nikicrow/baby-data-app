from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
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

def record(request, entry_id):
    response = "You're looking at the data record of entry %s."
    return HttpResponse(response % entry_id)