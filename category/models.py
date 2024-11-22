from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1500, blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} - {self.name}"
