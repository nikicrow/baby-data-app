from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # details
    path("toileting/<int:entry_id>", views.toilet_detail, name="toilet_detail"),
    path("feeding/<int:entry_id>", views.feeding_detail, name="feeding_detail"),
    path("sleeping/<int:entry_id>", views.toilet_detail, name="sleeping_detail"),
    path("growth/<int:entry_id>", views.feeding_detail, name="growth_detail"),
    # forms
    path("toilet_form/", views.toilet_form, name="toilet_form"),
    path("feeding_form/", views.feeding_form, name="feeding_form"),
    path("sleeping_form/", views.sleeping_form, name="sleeping_form"),
    path("growth_form/", views.growth_form, name="growth_form"),
    # delete
    path("toilet_delete/<int:entry_id>", views.toilet_delete, name="toilet_delete"),
    # edit
    path("toilet_edit/<int:entry_id>", views.toilet_edit, name="toilet_edit"),
]