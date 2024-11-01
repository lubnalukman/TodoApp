
from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
