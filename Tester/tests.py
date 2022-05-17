from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from Tester.views import tregister
# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_case_register_url(self):
        url=reverse("Tester:tregister")
        print(resolve(url))
        self.assertEquals(resolve(url).func,tregister)
