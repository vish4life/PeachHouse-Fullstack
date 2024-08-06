from django.test import TestCase
from PeachHouseApp.models import Menu
# Create your tests here.
class TestMenu(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="Basundi",price=12.99,inventory=100)
        itemstr = item.title
        self.assertEqual(itemstr,"Basundi")