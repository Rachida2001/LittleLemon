# tests/test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="Burger", price=10, inventory=50)
        self.menu_item2 = MenuItem.objects.create(title="Pizza", price=15, inventory=30)

    def test_getall(self):
        response = self.client.get('/menu/')
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
