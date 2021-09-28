from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile

"""
    Model for storing unique pass-code, and performing queries
    simply related to password handling.
"""
# class Pswd(models.Model):
#     passcode = models.CharField(max_length=150, null=True)
#     def __str__(self):
#         return self.passcode

"""
                        | Main model of this project |
    Model class for storing classname, class_creator, passcode reference & user_profile
    Here a field needs to be added which references all the users who have joined a
    particular class.
"""


class classroom(models.Model):
    id = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=50, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='creator', null=True
    )
    code = models.CharField(max_length=6, null=False, default="passwd")
    user_profile = models.ManyToManyField(UserProfile)

    def __str__(self):
        return self.classname
"""""

class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField(default=0)
    isbn13 = models.CharField(max_length=13,blank=True, null= True)

    def __str__(self):
        return self.title
"""""

class EBooksModel(models.Model):

    title = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='pdfs/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"



class Student(models.Model):
    name = models.CharField(max_length=191, null=True)
    studentId = models.CharField(max_length=12, null=True)
    age = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    course = models.CharField(max_length=191, null=True)
    phone = models.CharField(max_length=191, null=True)
    email = models.CharField(max_length=191, null=True)
    password = models.CharField(max_length=15, null=True)
    photo = models.ImageField()
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)


def __str__(self):
    return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=191, null=True)
    initials = models.CharField(max_length=10, null=True)
    course = models.CharField(max_length=191, null=True)
    phone = models.CharField(max_length=191, null=True)
    email = models.CharField(max_length=191, null=True)
    password = models.CharField(max_length=15, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

