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
    path("breast_feeding_form/", views.breast_feeding_form, name="breast_feeding_form"),
    path("bottle_feeding_form/", views.bottle_feeding_form, name="bottle_feeding_form"),
    path("sleeping_form/", views.sleeping_form, name="sleeping_form"),
    path("growth_form/", views.growth_form, name="growth_form"),
    # details
    path("toileting/<int:entry_id>", views.toilet_detail, name="toilet_detail"),
    path("breast_feeding/<int:entry_id>", views.breast_feeding_detail, name="breast_feeding_detail"),
    path("bottle_feeding/<int:entry_id>", views.bottle_feeding_detail, name="bottle_feeding_detail"),
    path("sleeping/<int:entry_id>", views.toilet_detail, name="sleeping_detail"),
    path("growth/<int:entry_id>", views.growth_detail, name="growth_detail"),
    # delete
    path("toilet_delete/<int:entry_id>", views.toilet_delete, name="toilet_delete"),
    path("breast_feed_delete/<int:entry_id>", views.breast_feed_delete, name="breast_feed_delete"),
    path("bottle_feed_delete/<int:entry_id>", views.bottle_feed_delete, name="bottle_feed_delete"),
    path("sleep_delete/<int:entry_id>", views.sleep_delete, name="sleep_delete"),
    path("growth_delete/<int:entry_id>", views.growth_delete, name="growth_delete"),
    # edit
    path("toilet_update/<int:entry_id>", views.toilet_update, name="toilet_update"),
    path("breast_feed_update/<int:entry_id>", views.breast_feed_update, name="breast_feed_update"),
    path("bottle_feed_update/<int:entry_id>", views.bottle_feed_update, name="bottle_feed_update"),
    path("sleep_update/<int:entry_id>", views.sleep_update, name="sleep_update"),
    path("growth_update/<int:entry_id>", views.growth_update, name="growth_update"),

]