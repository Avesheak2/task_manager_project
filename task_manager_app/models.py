from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    assignee = models.CharField(max_length=150)

    def __str__(self):
        return self.task_name

from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    assignee = models.ForeignKey('User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

from django.db import models
from .models import Task

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for {self.task.task_name}"
