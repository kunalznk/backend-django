from django.db import models
from user.models import User
# Create your models here.
class Message(models.Model):
    user_id = models.ForeignKey(
          User, 
          on_delete=models.CASCADE
  )
    message_id = models.TextField(unique=True)
    messsage = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)