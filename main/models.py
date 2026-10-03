from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30, blank=True)
    hometown = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField()
    favorite_subject = models.CharField(max_length=100)
    club = models.CharField(max_length=100, blank=True)
    motto = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
