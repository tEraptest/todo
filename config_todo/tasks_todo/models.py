from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f"Без названия"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title