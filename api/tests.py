from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, Review, Provider, User

class CourseAPITests(TestCase):
    def setUp(self):
        # Create test data
        self.client = APIClient()
        # Create a provider object (ensure it exists in the database)
        self.provider = Provider.objects.create(name='Test Provider', website='http://example.com', contact_info='test@example.com')
        self.course = Course.objects.create(title='Test Course', description='Test Description', duration='Test Duration', price=100, provider=self.provider)

    def test_get_courses(self):
        # Test GET request to retrieve list of courses
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure one course is returned

    def test_get_course_detail(self):
        # Test GET request to retrieve course detail
        response = self.client.get(reverse('course-detail', kwargs={'course_id': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Course')  # Ensure correct course is returned

class ReviewAPITests(TestCase):
    def setUp(self):
        # Create test data
        self.client = APIClient()
        # Create a user object (ensure it exists in the database)
        self.user = User.objects.create(username='test_user')
        # Create a provider object (ensure it exists in the database)
        self.provider = Provider.objects.create(name='Test Provider', website='http://example.com', contact_info='test@example.com')
        # Create a course object (ensure it exists in the database)
        self.course = Course.objects.create(title='Test Course', description='Test Description', duration='Test Duration', price=100, provider=self.provider)
    
    def test_create_review(self):
        # Test POST request to create a review
        data = {'user': self.user.id, 'rating': 5, 'review_text': 'Great course!'}
        response = self.client.post(reverse('review-list', kwargs={'course_id': 1}), data)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)  # Print serializer errors

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)  # Ensure review is created