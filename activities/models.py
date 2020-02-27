from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Activitie(models.Model):
    activitie = models.CharField(max_length=50)
    to_do_date = models.DateTimeField()
    is_done = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('activity-detail', kwargs={'pk': self.pk})

    

