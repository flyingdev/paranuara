from django.db import models
from django.contrib.postgres.fields.array import ArrayField

from company import models as comp_models


# Create your models here.
class Person(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICES = (
        (GENDER_MALE, GENDER_MALE),
        (GENDER_FEMALE, GENDER_FEMALE),
    )
    EYE_COLOR_BLUE = 'blue'
    EYE_COLOR_BROWN = 'brown'
    EYE_COLOR_CHOICES = (
        (EYE_COLOR_BLUE, EYE_COLOR_BLUE),
        (EYE_COLOR_BROWN, EYE_COLOR_BROWN),
    )
    has_died = models.BooleanField(default=False, null=False)
    balance = models.FloatField(null=True)
    picture = models.CharField(max_length=1024)
    age = models.IntegerField()
    eye_color = models.CharField(choices=EYE_COLOR_CHOICES, max_length=128)
    name = models.CharField(max_length=128)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=24)
    email = models.EmailField()
    phone = models.CharField(max_length=24)
    address = models.CharField(max_length=1024)
    about = models.CharField(max_length=1024)
    registered = models.DateTimeField()
    tags = ArrayField(models.CharField(max_length=128))
    greeting = models.CharField(max_length=1024)
    fruits = ArrayField(models.CharField(max_length=128))
    vegetables = ArrayField(models.CharField(max_length=128))
    company = models.ForeignKey(comp_models.Company, null=True, on_delete=models.SET_NULL, related_name='employees')
    friends = models.ManyToManyField('self')
    guid = models.UUIDField()
    _id = models.CharField(max_length=124)
    # TODO
    #     register company & friends using ManyToMany or ManyToOne or foreignkey
