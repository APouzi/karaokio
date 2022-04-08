from django.db import models
from django.conf import settings
 
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null = True)
    state = models.CharField(max_length=2, null=True)
    zip = models.IntegerField(null = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.name} and id: {self.id}"

