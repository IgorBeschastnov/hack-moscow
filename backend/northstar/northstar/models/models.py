from django.contrib.postgres import fields as pg
from django.db import models
# from .validators import
from .categories import categories_json


class CategoryChoices:

    @classmethod
    def make(cls):
        choice = []
        for category in categories_json:
            setattr(cls, category['id'].replace('-', '_').upper(), category['id'])
            choice.append((category['id'].replace('-', '_').upper(), category['title']))
        setattr(cls, 'CHOICES', choice)

    def to_list(self):
        return [choice[1] for choice in self.CHOICES]


CategoryChoices.make()


class SexChoices:
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'NB'
    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Nonbinary')
    )


class EventType:
    PUBLIC = 'PB'
    PRIVATE = 'PR'
    CHOICES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private')
    )


class Organization(models.Model):
    title = models.CharField(max_length=50, null=False)
    login = models.CharField(max_length=100, null=False, unique=True)
    password = models.BinaryField(max_length=32, null=False)
    address = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False, choices=CategoryChoices.CHOICES)
    long = models.FloatField(null=True)
    lat = models.FloatField(null=True)


class User(models.Model):
    uid = models.CharField(max_length=100, null=False, unique=True)
    sex = models.CharField(max_length=100, null=True, choices=SexChoices.CHOICES)
    age = models.IntegerField(null=True)


class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)
    type = models.CharField(max_length=100, null=True, choices=EventType.CHOICES)
    long = models.FloatField(null=False)
    lat = models.FloatField(null=False)


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    category = models.CharField(max_length=100, null=False, choices=CategoryChoices.CHOICES)
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)


class PlacesStatistics(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    data = pg.JSONField()
