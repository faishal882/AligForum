from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=220, null=True, blank=True)
    faculty = models.CharField(max_length=220, null=True, blank=True)
    course = models.CharField(max_length=220, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=GENDER_CHOICES,
        default='Male'
    )

    class Meta:
        ordering = ['-id']


def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(name=instance)


post_save.connect(user_did_save, sender=User)
