from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=30)
    heroku_id = models.CharField(max_length=45)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=50)
    heroku_id = models.CharField(max_length=45)
    films = models.ManyToManyField(Film)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class LastUpdated(models.Model):
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.time)
