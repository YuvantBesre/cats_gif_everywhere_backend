from django.db import models

# Create your models here.
class CatData(models.Model):
    type = models.SlugField(null = True, blank = True)
    title = models.CharField(max_length = 300)
    position = models.PositiveSmallIntegerField(default = 0)
    image = models.FileField(upload_to = 'cats_everywhere/')
    created = models.DateTimeField(auto_now_add=True, help_text='When this record is created!')
    updated = models.DateTimeField(auto_now=True, help_text='When this record was modified!')
