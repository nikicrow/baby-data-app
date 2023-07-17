from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
class Toileting(models.Model):
    pee = models.BooleanField(default=False)
    pee_scale = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    poo = models.BooleanField(default=False)
    poo_scale = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    poo_colour = models.CharField(default='brown')
    toilet_time = models.DateTimeField("toilet time",default = timezone.now())
    notes = models.CharField(max_length=200, default='n/a', null=True)

    @admin.display(
        boolean=True,
        ordering="toilet_time",
        description="Recorded recently?",
    )

    # when we call the model lets return something helpful to identify the object
    def __str__(self):
        return self.toilet_time.strftime("%m/%d/%Y, %H:%M")
    
    # return entries recorded in past 24 hours
    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.toilet_time <= now


class Feeding(models.Model):
    right_boob_first = models.BooleanField(default=False)
    right_boob_time = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    left_boob_first = models.BooleanField(default=False)
    left_boob_time =  models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    feed_time = models.DateTimeField("feed time",default = timezone.now())
    notes = models.CharField(max_length=200, default='n/a', null=True)

    @admin.display(
        boolean=True,
        ordering="feed_time",
        description="Recorded recently?",
    )


    # when we call the model lets return something helpful to identify the object
    def __str__(self):
        return self.feed_time.strftime("%m/%d/%Y, %H:%M")
    
    # return entries recorded in past 24 hours and not in the future
    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.feed_time <= now
    

class Sleeping(models.Model):
    nap_length =  models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    nap_start_time = models.DateTimeField("nap start time",default = timezone.now())
    nap_quality = models.CharField(max_length=200, default='medium', null=True)
    nap_location = models.CharField(max_length=200, default='bedroom', null=True)
    notes = models.CharField(max_length=200, default='n/a', null=True)

    @admin.display(
        boolean=True,
        ordering="nap_start_time",
        description="Recorded recently?",
    )

    # when we call the model lets return something helpful to identify the object
    def __str__(self):
        return self.nap_start_time.strftime("%m/%d/%Y, %H:%M")
    
    # return entries recorded in past 24 hours and not in the future
    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.nap_start_time <= now
    

class Growth(models.Model):
    head_circumference =  models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    height =  models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    weight =  models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    measurement_time = models.DateTimeField("growth measure time",default = timezone.now())
    notes = models.CharField(max_length=200, default='n/a', null=True)

    @admin.display(
        boolean=True,
        ordering="measurement_time",
        description="Recorded recently?",
    )

    # when we call the model lets return something helpful to identify the object
    def __str__(self):
        return self.measurement_time.strftime("%m/%d/%Y, %H:%M")
    
    # return entries recorded in past 24 hours and not in the future
    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.measurement_time <= now