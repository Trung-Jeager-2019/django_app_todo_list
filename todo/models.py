from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    # objects = models.Manager()
    def __str__(self):
        return self.name
