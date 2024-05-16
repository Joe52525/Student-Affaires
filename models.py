from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields you need

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields you need

    def __str__(self):
        return self.name
