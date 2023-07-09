from django.contrib import admin

# Register your models here.
from .models import Toileting, Feeding

class ToiletingAdmin(admin.ModelAdmin):
    list_filter = ["toilet_time"]
    list_display = ["toilet_time", "pee","pee_scale", "poo","poo_scale", "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["toilet_time"]}),
        ("Pee" , {"fields":["pee","pee_scale"]}),
        ("Poo" , {"fields":["poo","poo_scale"]}),
        (None, {"fields": ["notes"]}), 
        ]

class FeedingAdmin(admin.ModelAdmin):
    list_filter = ["feed_time"]
    list_display = ["feed_time", "right_boob_first","right_boob_time", "left_boob_first","left_boob_time", "was_recorded_recently","notes"]
    fieldsets = [
        ("Date information", {"fields":["feed_time"]}),
        ("Right boob" , {"fields":["right_boob_first","right_boob_time"]}),
        ("Left boob" , {"fields":["left_boob_first","left_boob_time"]}),
        (None, {"fields": ["notes"]}), 
        ]

admin.site.register(Toileting, ToiletingAdmin)
admin.site.register(Feeding, FeedingAdmin)