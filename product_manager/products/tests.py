from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTests(TestCase):

    def setUp(self):
        # Create a user to test login
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_page_status_code(self):
        """
        Test that the login page returns a status code of 200.
        """
        response = self.client.get(reverse('products:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_uses_correct_template(self):
        """
        Test that the login page uses the correct template.
        """
        response = self.client.get(reverse('products:login'))
        self.assertTemplateUsed(response, 'registration/login.html')