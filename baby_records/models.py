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
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    poo = models.BooleanField(default=False)
    poo_scale = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    # poo_colour 
    toilet_time = models.DateTimeField("toilet time")
    notes = models.CharField(max_length=200, default='n/a', null=True, blank=True)

    @admin.display(
        boolean=True,
        ordering="toilet_time",
        description="Recorded recently?",
    )

    # when we call the model lets return something helpful to identify the object
    def __str__(self):
        return self.toilet_time.strftime("%m/%d/%Y, %H:%M:%S")
    
    # return entries recorded in past 24 hours
    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.toilet_time <= now


class Feeding(models.Model):
    right_boob_first = models.BooleanField(default=False)
    right_boob_time = models.IntegerField(default=0)
    left_boob_first = models.BooleanField(default=False)
    left_boob_time =  models.IntegerField(default=0)
    feed_time = models.DateTimeField("feed time")
    notes = models.CharField(max_length=200, default='n/a', null=True, blank=True)

    @admin.display(
        boolean=True,
        ordering="feed_time",
        description="Recorded recently?",
    )


    # when we call the model lets return something helpful to identify the object
    def __str__(self):
        return self.feed_time.strftime("%m/%d/%Y, %H:%M:%S")
    
    # return entries recorded in past 24 hours and not in the future
    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.feed_time <= now
    
class ToiletingForm(ModelForm):
    class Meta:
        model = Toileting
        fields = "__all__"


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = "__all__"