from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# Create your tests here.
from .models import Members


class BaseTest(TestCase):
   
    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "Benson Njunge"
        self.email= "bensonnjung39@gmail.com"
        self.interests="I love food and travelling"
        self.member = Members(name=self.name,email=self.email,interests=self.interests)
        self.client = APIClient()
        self.member_data = {'name':self.name,'email':self.email,'interests':self.interests}
        self.response = self.client.post(
            reverse('create'),
            self.member_data,
            format="json")

class ModelTestCase(BaseTest):
    """This class defines the test suite for the members model."""


    def test_model_can_create_a_member(self):
        """Test the members mode can create a member."""
        old_count=Members.objects.count()
        self.member.save()
        new_count=Members.objects.count()
        self.assertNotEqual(old_count,new_count)

    
# Define this after the ModelTestCase
class ViewTestCase(BaseTest):
    """Test suite for the api views."""

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)