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


GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("other", "OTHER"),
)


class Teacher(TimeStamp):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="teacher")
    education = models.CharField(max_length=50)
    slc_marksheet = models.FileField(upload_to="slc")
    plus2_transcript = models.FileField(upload_to="plus2")
    bachelor_marksheet = models.FileField(upload_to="bachelor")
    cv = models.FileField(upload_to="cv")
    about = models.TextField()

    def __str__(self):
        return self.name
