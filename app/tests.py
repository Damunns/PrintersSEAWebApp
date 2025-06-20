from django.test import TestCase
from django.contrib.auth.models import User

from .models import Printer 

class CRUDTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_object = Printer.objects.create(
            brand="Test Brand",
            model="Test Model",
            location="Test Location",
            ip_address="192.168.1.1",
            mac_address="00:1A:2B:3C:4D:5E",
            manufacture_date="2025-06-20",
            comments="Test comments"
        )

    def test_create(self):
        """Test creating an object."""
        obj = Printer.objects.create(
            brand="Create Brand",
            model="Create Model",
            location="Create Location",
            ip_address="192.168.1.2",
            mac_address="00:1A:2B:3C:4D:5F",
            manufacture_date="2025-06-21",
            comments="Create comments"
        )
        self.assertEqual(obj.brand, "Create Brand")
        self.assertEqual(obj.model, "Create Model")
        self.assertEqual(obj.location, "Create Location")
        self.assertEqual(obj.ip_address, "192.168.1.2")
        self.assertEqual(obj.mac_address, "00:1A:2B:3C:4D:5F")
        self.assertEqual(obj.manufacture_date, "2025-06-21")
        self.assertEqual(obj.comments, "Create comments")

    def test_read(self):
        """Test reading an object."""
        obj = Printer.objects.get(brand='Test Brand')
        self.assertEqual(obj.brand, 'Test Brand')

    def test_update(self):
        """Test updating an object."""
        self.test_object.brand = 'Update Brand'
        self.test_object.save()
        self.assertEqual(self.test_object.brand, 'Update Brand')

    def test_delete(self):
        """Test deleting an object."""
        self.test_object.delete()
        with self.assertRaises(Printer.DoesNotExist):
            Printer.objects.get(brand='Test Brand')

class UserAuthTest(TestCase):
    def setUp(self):
        """Set up test user."""
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        """Test user login."""
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)

    def test_logout(self):
        """Test user logout."""
        self.client.login(username='testuser', password='testpassword')
        self.client.logout()
        response = self.client.get('/')
        self.assertNotContains(response, 'testuser')