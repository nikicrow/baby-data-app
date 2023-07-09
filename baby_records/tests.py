# Create your tests here.
# to run tests use 'manage.py test baby_records'
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Toileting, Feeding


class ToiletingModelTests(TestCase):
    def test_was_published_recently_with_future_toileting(self):
        """
        was_recorded_recently() returns False for toilet sessions whose toilet_time
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_toilet_session = Toileting(toilet_time=time)
        self.assertIs(future_toilet_session.was_recorded_recently(), False)


class FeedingModelTests(TestCase):
    def test_was_published_recently_with_future_feeding(self):
        """
        was_recorded_recently() returns False for feeding sessions whose feed_time
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_feeding_session = Feeding(feed_time=time)
        self.assertIs(future_feeding_session.was_recorded_recently(), False)