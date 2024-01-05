# blog/tests.py
from django.test import TestCase
from .models import blog
from django.urls import reverse
class BlogModelTest(TestCase):

    def setUp(self):
        blog.objects.create(text='Just a test case')

    def test_text_content(self):
        blog_instance = blog.objects.get(id=1)  # Use a different variable name
        expected_object_name = f'{blog_instance.text}'
        self.assertEqual(expected_object_name, 'Just a test case')  # Correct the expected value


#HomePageView Tests
class HomePageViewTest(TestCase): 
    def setUp(self):
        blog.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')