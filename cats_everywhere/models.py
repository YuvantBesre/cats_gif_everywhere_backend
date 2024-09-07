from django.db import models
from .utils import unique_slug_generator

# Create your models here.
class CatData(models.Model):
    type = models.SlugField(null = True, blank = True)
    title = models.CharField(max_length = 300)
    position = models.PositiveSmallIntegerField(default = 0)
    image = models.FileField()
    created = models.DateTimeField(auto_now_add=True, help_text='When this record is created!')
    updated = models.DateTimeField(auto_now=True, help_text='When this record was modified!')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.type = unique_slug_generator(self, 'title')
        super().save(*args, **kwargs)
