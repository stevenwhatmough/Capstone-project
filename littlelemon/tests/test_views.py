from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.views import MenuView
from restaurant.serializers import MenuSerializer

from rest_framework.test import APIRequestFactory, force_authenticate

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        Menu.objects.create(Title="salad", Price=3.25, Inventory=2)
        Menu.objects.create(Title="soup", Price=4.50, Inventory=5)


    def test_getall(self):
        request = self.factory.get('/menu')
        force_authenticate(request, user=self.user)

        response = MenuView.as_view()(request)

        items = Menu.objects.all()
        serialized_data=MenuSerializer(items, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)