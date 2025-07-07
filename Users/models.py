from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Candidates(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate')
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='candidates/', null=True, blank=True)
    votes = models.PositiveIntegerField(default=0)
    percentege = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - {self.position}"

    class Meta:
        verbose_name_plural = "Candidates"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    voted_personero = models.BooleanField(default=False)
    voted_contralor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Profile"
    
    class Meta:
        verbose_name_plural = "Profiles"