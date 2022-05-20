from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.TextField(unique=True)
    user_name = models.TextField()
    user_email = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)