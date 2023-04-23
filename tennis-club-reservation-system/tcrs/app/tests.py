from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MemberProfile, Reservation
from .forms import ReservationForm

# tests to check if page exists
class HomePageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class AccountPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/account/")
        self.assertEqual(response.status_code, 302)

class ReservationsPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 302)

class MemebershipPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/membership/")
        self.assertEqual(response.status_code, 302)

class PaymentPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/payment/")
        self.assertEqual(response.status_code, 302)

class BillingPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/billing/")
        self.assertEqual(response.status_code, 302)

class DirectoryPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/directory/")
        self.assertEqual(response.status_code, 302)

class Guest_InfoPageExists(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/guest_info/")
        self.assertEqual(response.status_code, 302)

# functional tests
class FunctionalTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.reservation_url = reverse('reservations')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.member_profile = MemberProfile.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            address ='200 Bloomfield Ave',
            phone_number='123-456-7890',
            date_of_birth='2001-01-01',
            in_directory=False
        )
        self.reservation = Reservation.objects.create(
            user=self.user,
            date='2023-04-24',
            time='10:00',
            court='1',
            number_of_players=1,
            number_of_guests=0,
            is_tournament=False
        )

    def test_reservation_page_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.reservation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')
        self.assertTrue(response.context['is_member'])
        self.assertFalse(response.context['reservation_failed'])
        self.assertIsInstance(response.context['form'], ReservationForm)

    def test_reservation_page_view_with_unauthenticated_user(self):
        response = self.client.get(self.reservation_url)
        self.assertRedirects(response, self.signup_url + '?next=' + self.reservation_url)
        self.assertEqual(response.status_code, 302)

    def test_reservation_page_view_with_post_request(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'date': '2023-04-24',
            'time': '10:00',
            'court': '1',
            'number_of_players': '1',
            'number_of_guests': '0',
            'is_tournament': 'False'
        }
        response = self.client.post(self.reservation_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(str(Reservation.objects.last().date), '2023-04-24')
        self.assertEqual(str(Reservation.objects.last().time), '10:00:00')
        self.assertEqual(str(Reservation.objects.last().court), '1')
        self.assertEqual(Reservation.objects.last().number_of_players, 1)
        self.assertEqual(Reservation.objects.last().number_of_guests, 0)

    def test_reservation_page_view_with_post_request_and_reservation_conflict(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'date': '2023-04-24',
            'time': '10:00',
            'court': '1',
            'number_of_players': '1',
            'number_of_guests': '0',
            'is_tournament': 'False'
        }
        response = self.client.post(self.reservation_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')
        self.assertTrue(response.context['reservation_failed'] == True)
        self.assertEqual(Reservation.objects.count(), 1)

    def tearDown(self):
        self.client.logout()
