from django.db import models


class Teacher(models.Model):

    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE
    )

    nip = models.CharField(
        max_length=30,
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()