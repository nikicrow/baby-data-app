from django.contrib import admin

# Register your models here.
from .models import Toileting, BreastFeeding, BottleFeeding, Sleeping, Growth

class ToiletingAdmin(admin.ModelAdmin):
    list_filter = ["toilet_time"]
    list_display = ["toilet_time", "pee","pee_scale", "poo","poo_scale", "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["toilet_time"]}),
        ("Pee" , {"fields":["pee","pee_scale"]}),
        ("Poo" , {"fields":["poo","poo_scale"]}),
        (None, {"fields": ["was_recorded_recently","notes"]}), 
        ]

class BreastFeedingAdmin(admin.ModelAdmin):
    list_filter = ["feed_time"]
    list_display = ["feed_time", "which_boob_first","right_boob_time", "left_boob_time", "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["feed_time"]}),
        ("Which boob" , {"fields":["which_boob_first"]}),
        ("Time on boob" , {"fields":["right_boob_time","left_boob_time"]}),
        (None, {"fields": ["was_recorded_recently","notes"]}), 
        ]

class BottleFeedingAdmin(admin.ModelAdmin):
    list_filter = ["feed_time"]
    list_display = ["feed_time", "drinking_ml","drinking_time",  "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["feed_time"]}),
        ("Amount feeding" , {"fields":["drinking_ml"]}),
        ("Time feeding" , {"fields":["drinking_time"]}),
        (None, {"fields": ["was_recorded_recently","notes"]}), 
        ]
    
class SleepingAdmin(admin.ModelAdmin):
    list_filter = ["nap_start_time"]
    list_display = ["nap_start_time", "nap_length","nap_quality", "nap_location", "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["nap_start_time"]}),
        ("Nap details" , {"fields":["nap_length","nap_quality", "nap_location"]}),
        (None, {"fields": ["was_recorded_recently","notes"]}), 
        ]
    
class GrowthAdmin(admin.ModelAdmin):
    list_filter = ["measurement_time"]
    list_display = ["measurement_time", "head_circumference","height", "weight", "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["measurement_time"]}),
        ("Measurement details" , {"fields":["head_circumference","height", "weight"]}),
        (None, {"fields": ["was_recorded_recently","notes"]}), 
        ]

admin.site.register(Toileting, ToiletingAdmin)
admin.site.register(BreastFeeding, BreastFeedingAdmin)
admin.site.register(BottleFeeding, BottleFeedingAdmin)
admin.site.register(Sleeping, SleepingAdmin)
admin.site.register(Growth, GrowthAdmin)