from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class HomeTuitionSystem(TimeStamp):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    about = models.TextField()

    def __str__(self):
        return self.name
