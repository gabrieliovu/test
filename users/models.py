from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    class Gender:
        MALE = 'M'
        FEMALE = 'F'

    GENDER_CHOICES = (
        (Gender.MALE, _('M')),
        (Gender.FEMALE, _('F'))
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    industry = models.CharField(max_length=128, null=True, blank=True)
    salary = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    years_of_experience = models.PositiveSmallIntegerField(blank=True, null=True)
