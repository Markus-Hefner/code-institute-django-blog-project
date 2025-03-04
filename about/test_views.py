from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAbout(TestCase):

    def setUp(self):
        self.about = About(title="Guybrush Threepwood", profile_image="placeholder", 
                           content="GT is a mighty pirate!", updated_on="It's up to date") # The profile image and updated on fields are not needed
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Guybrush Threepwood", response.content)
        self.assertIn(b"GT is a mighty pirate!", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
        
    def test_successful_collaboration_request_submission(self):
        """Test for successfully sending a collaboration_request"""
        post_data = {
            'name': 'Test Requester',
            'email': 'test@requester.com',
            'message': 'This is a test request.'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )
