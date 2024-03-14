# In your app's models.py file
from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    contact_info = models.CharField(max_length=200)
    class Meta:
        app_label = 'api'

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    class Meta:
        app_label = 'api'

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(Instructor)
    class Meta:
        app_label = 'api'

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Encrypted password
    class Meta:
        app_label = 'api'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    class Meta:
        app_label = 'api'