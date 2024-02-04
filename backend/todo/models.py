from django.db import models
from django.utils import timezone
from datetime import timedelta

class Todo(models.Model):
    title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 500)
    deadline = models.DateField(default=timezone.now() + timedelta(days=1))
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title