from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Personero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    vote = models.IntegerField(max_length=50, default=0)
    image = models.ImageField(upload_to='candidates/')

    def __str__(self):
        return f"{self.user.username} - Candidato a personero"
    
    class Meta:
        verbose_name_plural = "Candidates"
        
class Contralor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contralor_profile')
    vote = models.IntegerField(max_length=50, default=0)
    image = models.ImageField(upload_to='candidates/')

    def __str__(self):
        return f"{self.user.username} - Candidato a contralor"
    
    class Meta:
        verbose_name_plural = "Contralores"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    voted_personero = models.BooleanField(default=False)
    voted_contralor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Profile"
    
    class Meta:
        verbose_name_plural = "Profiles"