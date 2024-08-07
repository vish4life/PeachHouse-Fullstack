from django.test import TestCase
from PeachHouseApp.models import Menu,Booking
from django.utils import timezone
# Create your tests here.
class TestMenu(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="Cheesecake",price=12.99,inventory=100)
        itemstr = item.title
        self.assertEqual(itemstr,"Cheesecake")
class TestBooking(TestCase):
    def test_get_booking(self):
        bookings=Booking.objects.create(name="UnitTest001",no_of_guests=2,booking_date=timezone.now())
        bookedName=bookings.name
        self.assertEqual(bookedName,"UnitTest001")