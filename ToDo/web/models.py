from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES=[
        ('l','LOW'),
        ('m','Medium'),
        ('h','Hight')
    ]
    TASKLEVEL_CHOICES=[
        (-1,'TODO'),
        (0,'Doing'),
        (1,'Done')
    ]
    title=models.CharField(max_length=255)
    text=models.TextField(max_length=500)
    priority=models.CharField(max_length=1,choices=PRIORITY_CHOICES)
    level=models.IntegerField(choices=TASKLEVEL_CHOICES)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    create_date=models.DateField(default=timezone.now)
    due_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
