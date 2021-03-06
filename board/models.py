from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    visibleYn = models.BooleanField(default=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.visibleYn = True
        self.save()
    
    def __str__(self):
        return self.title
