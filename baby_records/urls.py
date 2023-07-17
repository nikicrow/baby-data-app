from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # details
    path("<int:entry_id>/toileting", views.toilet_detail, name="toilet_detail"),
    path("<int:entry_id>/feeding", views.feeding_detail, name="feeding_detail"),
    path("<int:entry_id>/sleeping", views.toilet_detail, name="sleeping_detail"),
    path("<int:entry_id>/growth", views.feeding_detail, name="growth_detail"),
    # forms
    path("toilet_form/", views.toilet_form, name="toilet_form"),
    path("feeding_form/", views.feeding_form, name="feeding_form"),
    path("sleeping_form/", views.sleeping_form, name="sleeping_form"),
    path("growth_form/", views.growth_form, name="growth_form"),
]