from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    course_title = models.CharField(max_length=30)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=35)
    course_duration = models.DecimalField(max_digits=1000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.course_title


