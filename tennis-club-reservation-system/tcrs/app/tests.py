from django.test import TestCase
from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class AccountpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/account/")
        self.assertEqual(response.status_code, 200)

class ReservationpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)

class MembershippageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/membership/")
        self.assertEqual(response.status_code, 200)
