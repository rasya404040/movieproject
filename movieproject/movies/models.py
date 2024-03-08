from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=40)
    desc=models.TextField(max_length=200)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movies/poster",null=True,blank=True)

    def __str__(self):
        return self.name
