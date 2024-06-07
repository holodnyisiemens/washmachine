from django.db import models
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('services', kwargs={'service_slug': self.slug})
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
