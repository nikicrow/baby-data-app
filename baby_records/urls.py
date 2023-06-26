from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /baby_records/5/
    path("<int:entry_id>/", views.detail, name="detail"),
    # ex: /baby_records/5/record/
    path("<int:entry_id>/record/", views.record, name="record"),
]