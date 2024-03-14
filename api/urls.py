from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:course_id>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/search/', views.CourseSearchView.as_view(), name='course-search'),
    path('users/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('courses/<int:course_id>/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('courses/<int:course_id>/reviews/<int:review_id>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('providers/', views.ProviderListView.as_view(), name='provider-list'),
    path('providers/<int:provider_id>/', views.ProviderDetailView.as_view(), name='provider-detail'),
    path('instructors/', views.InstructorListView.as_view(), name='instructor-list'),
    path('instructors/<int:instructor_id>/', views.InstructorDetailView.as_view(), name='instructor-detail'),
]
