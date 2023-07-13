from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /baby_records/5/
    path("<int:entry_id>/", views.detail, name="detail"),
    # ex: /baby_records/5/toilet_record/
    path("<int:entry_id>/toilet_record/", views.toilet_record, name="toilet_record"),
    path("toilet_form/", views.toilet_form, name="toilet_form"),
]