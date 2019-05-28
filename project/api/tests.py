from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.reverse import reverse
from rest_framework import status

from django.contrib.auth.models import User

factory = APIRequestFactory()
request = factory.get('/')


class ApiTest(APITestCase):

    def setUp(self):
        pass

    def test_login_with_invalid_credentials(self):
        payload = {
            "email": "wrong@bika54.com",
            "password": "P@ssw0rd"
        }

        response = self.client.post(reverse('rest_login'), data=payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["non_field_errors"], ["Unable to log in with provided credentials."])

    def test_login_with_valid_credentials_returns_token_and_user_data(self):
        user = User.objects.create_user("clodo", "clodo@bika54.com", "P@ssw0rd")
        user.first_name = "Claudio"
        user.last_name = "Bidau"
        user.save()

        payload = {
            "email": "clodo@bika54.com",
            "password": "P@ssw0rd"
        }

        response = self.client.post(reverse('rest_login'), payload)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["token"])
        self.assertEqual(response.data["user"], {
            "pk": 1,
            "username": "clodo",
            "email": "clodo@bika54.com",
            "first_name": "Claudio",
            "last_name": "Bidau"
        })


# api/v1/rest-auth/password/reset/
# api/v1/rest-auth/password/reset/confirm/
# api/v1/rest-auth/login/
# api/v1/rest-auth/logout/
# api/v1/rest-auth/user/
# api/v1/rest-auth/password/change/
