from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import UserProfile
from rest_framework.reverse import reverse as api_reverse
from rest_framework import  status

# Create your tests here.

User = get_user_model()
class userAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testuser', email='test@test.com')
        user_obj.set_password("randompassword")
        user_obj.save()
        customuser = UserProfile.objects.create(
            user=user_obj,
            description = 'random'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count,1)

    def test_single_post(self):
        post_count = UserProfile.objects.count()
        self.assertEqual(post_count,1)

    def test_get_list(self):
        data = {}
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.get(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        print(response.data)

    def test_post_list(self):
        data = {}
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.get(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        print(response.data)