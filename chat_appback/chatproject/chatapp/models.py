from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class chat(models.Model):
    message=models.TextField()
    from_user=models.ForeignKey(User,related_name="from_user_message",on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name="to_user_message",on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    
    
