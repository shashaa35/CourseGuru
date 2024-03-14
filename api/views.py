from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Course, User, Review, Provider, Instructor
from .serializers import (
    CourseSerializer,
    UserSerializer,
    ReviewSerializer,
    ProviderSerializer,
    InstructorSerializer,
)
from django.utils.datastructures import MultiValueDict

class CourseListView(APIView):
    @swagger_auto_schema(
        operation_summary="List all courses",
        responses={200: CourseSerializer(many=True)}
    )
    def get(self, request):
        """
        Get a list of all courses.
        """
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Get details of a course",
        responses={200: CourseSerializer()}
    )
    def get(self, request, course_id):
        """
        Get details of a specific course.
        """
        course = Course.objects.get(pk=course_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

class CourseSearchView(APIView):
    @swagger_auto_schema(
        operation_summary="Search courses",
        manual_parameters=[
            openapi.Parameter('query', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING)
        ],
        responses={200: CourseSerializer(many=True)}
    )
    def get(self, request):
        """
        Search for courses based on a query string.
        """
        query = request.query_params.get('query', '')
        courses = Course.objects.filter(title__icontains=query)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class UserRegistrationView(APIView):
    @swagger_auto_schema(
        operation_summary="Register a new user",
        request_body=UserSerializer,
        responses={201: UserSerializer()}
    )
    def post(self, request):
        """
        Register a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ReviewListView(APIView):
    @swagger_auto_schema(
        operation_summary="Get reviews for a course",
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request, course_id):
        """
        Get reviews for a specific course.
        """
        reviews = Review.objects.filter(course_id=course_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a review for a course",
        responses={201: ReviewSerializer()}
    )
    def post(self, request, course_id):
        """
        Create a review for a specific course.
        """
        mutable_data = MultiValueDict(request.data)
        mutable_data['course'] = course_id
        serializer = ReviewSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Get details of a review",
        responses={200: ReviewSerializer()}
    )
    def get(self, request, course_id, review_id):
        """
        Get details of a specific review.
        """
        review = Review.objects.get(course_id=course_id, pk=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update a review",
        responses={200: ReviewSerializer()}
    )
    def put(self, request, course_id, review_id):
        """
        Update details of a specific review.
        """
        review = Review.objects.get(course_id=course_id, pk=review_id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a review",
        responses={204: "No Content"}
    )
    def delete(self, request, course_id, review_id):
        """
        Delete a specific review.
        """
        review = Review.objects.get(course_id=course_id, pk=review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProviderListView(APIView):
    @swagger_auto_schema(
        operation_summary="Get list of providers",
        responses={200: ProviderSerializer(many=True)}
    )
    def get(self, request):
        """
        Get a list of all providers.
        """
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

class ProviderDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Get details of a provider",
        responses={200: ProviderSerializer()}
    )
    def get(self, request, provider_id):
        """
        Get details of a specific provider.
        """
        provider = Provider.objects.get(pk=provider_id)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

class InstructorListView(APIView):
    @swagger_auto_schema(
        operation_summary="Get list of instructors",
        responses={200: InstructorSerializer(many=True)}
    )
    def get(self, request):
        """
        Get a list of all instructors.
        """
        instructors = Instructor.objects.all()
        serializer = InstructorSerializer(instructors, many=True)
        return Response(serializer.data)

class InstructorDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Get details of an instructor",
        responses={200: InstructorSerializer()}
    )
    def get(self, request, instructor_id):
        """
        Get details of a specific instructor.
        """
        instructor = Instructor.objects.get(pk=instructor_id)
        serializer = InstructorSerializer(instructor)
        return Response(serializer.data)