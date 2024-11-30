from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    venue = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)  # New time field
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
