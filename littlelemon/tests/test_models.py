from django.test import TestCase
from littlelemonapi.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem(title='Test Item', price=10, inventory=10)
        self.assertEqual(item.get_item(), 'Test Item : 10')