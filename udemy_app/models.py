from django.db import models

# Create your models here.

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    url = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_timestamp = models.DateTimeField()
    subject = models.CharField(max_length=50)