from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # main page
    path("main_toilet/", views.toilet_main_page, name="main_toilet"),
    path("main_feed/", views.feed_main_page, name="main_feed"),
    path("main_sleep/", views.sleep_main_page, name="main_sleep"),
    path("main_growth/", views.growth_main_page, name="main_growth"),
    # forms
    path("toilet_form/", views.toilet_form, name="toilet_form"),
    path("feeding_form/", views.feeding_form, name="feeding_form"),
    path("sleeping_form/", views.sleeping_form, name="sleeping_form"),
    path("growth_form/", views.growth_form, name="growth_form"),
    # details
    path("toileting/<int:entry_id>", views.toilet_detail, name="toilet_detail"),
    path("feeding/<int:entry_id>", views.feeding_detail, name="feeding_detail"),
    path("sleeping/<int:entry_id>", views.toilet_detail, name="sleeping_detail"),
    path("growth/<int:entry_id>", views.feeding_detail, name="growth_detail"),
    # delete
    path("toilet_delete/<int:entry_id>", views.toilet_delete, name="toilet_delete"),
    path("feed_delete/<int:entry_id>", views.feed_delete, name="feed_delete"),
    path("sleep_delete/<int:entry_id>", views.sleep_delete, name="sleep_delete"),
    path("growth_delete/<int:entry_id>", views.growth_delete, name="growth_delete"),
    # edit
    path("toilet_update/<int:entry_id>", views.toilet_update, name="toilet_update"),
    path("feed_update/<int:entry_id>", views.feed_update, name="feed_update"),
    path("sleep_update/<int:entry_id>", views.sleep_update, name="sleep_update"),
    path("growth_update/<int:entry_id>", views.growth_update, name="growth_update"),

]