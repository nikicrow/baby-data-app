from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # details
    path("<int:entry_id>/toileting", views.toilet_detail, name="toilet_detail"),
    path("<int:entry_id>/feeding", views.feeding_detail, name="feeding_detail"),
    # forms
    path("toilet_form/", views.toilet_form, name="toilet_form"),
    path("feeding_form/", views.feeding_form, name="feeding_form"),
]