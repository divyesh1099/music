from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        default='male',
    )

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.name