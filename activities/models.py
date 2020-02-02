from django.db import models

class Activity(models.Model):
    activity = models.CharField(max_length=50)
    to_do_date = models.DateTimeField()
    is_done = models.BooleanField()

