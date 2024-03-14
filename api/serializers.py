from rest_framework import serializers
from .models import Provider, Instructor, Course, User, Review

class ProviderSerializer(serializers.ModelSerializer):
    """
    Serializer for Provider model.
    """
    class Meta:
        model = Provider
        fields = ['id', 'name', 'website', 'contact_info']
        extra_kwargs = {
            'name': {'help_text': 'The name of the provider.'},
            'website': {'help_text': 'The website URL of the provider.'},
            'contact_info': {'help_text': 'Contact information for the provider.'}
        }

class InstructorSerializer(serializers.ModelSerializer):
    """
    Serializer for Instructor model.
    """
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'provider']
        extra_kwargs = {
            'name': {'help_text': 'The name of the instructor.'},
            'provider': {'help_text': 'The provider associated with the instructor.'}
        }

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.
    """
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'price', 'provider', 'instructors']
        extra_kwargs = {
            'title': {'help_text': 'The title of the course.'},
            'description': {'help_text': 'A description of the course.'},
            'duration': {'help_text': 'The duration of the course in hours.'},
            'price': {'help_text': 'The price of the course.'},
            'provider': {'help_text': 'The provider offering the course.'},
            'instructors': {'help_text': 'Instructors teaching the course.'}
        }

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'username': {'help_text': 'The username of the user.'},
            'email': {'help_text': 'The email address of the user.'},
            'password': {'help_text': 'The password of the user.'}
        }

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Review model.
    """
    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', 'review_text']
        extra_kwargs = {
            'user': {'help_text': 'The user who submitted the review.'},
            'course': {'help_text': 'The course being reviewed.'},
            'rating': {'help_text': 'The rating given for the course.'},
            'review_text': {'help_text': 'The text of the review.'}
        }

    def validate_rating(self, value):
        """
        Validate rating field to ensure it's between 0 and 5.
        """
        if value < 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value
