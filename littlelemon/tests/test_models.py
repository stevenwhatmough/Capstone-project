from restaurant.models import Menu
from django.test import TestCase

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="biscuit", Price=2.52, Inventory=2)
        itemstr = str(item)
        
        self.assertEqual(itemstr, "biscuit : 2.52")