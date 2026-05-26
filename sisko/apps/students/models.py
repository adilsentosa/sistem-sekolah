from django.db import models


class Parent(models.Model):

    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    def __str__(self):
        return self.user.get_full_name()

class Student(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    nis = models.CharField(
        max_length=20,
        unique=True
    )

    nisn = models.CharField(
        max_length=20,
        unique=True
    )

    full_name = models.CharField(
        max_length=100
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )

    birth_date = models.DateField()

    address = models.TextField()

    parent = models.ForeignKey(
        Parent,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    classroom = models.ForeignKey(
        'academics.Classroom',
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name