#from django.db import models

# Create your models here.
from django.db import models

class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now=True)
    

    def _str_(self):
        return self.title