from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):    
    id = models.IntegerField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()