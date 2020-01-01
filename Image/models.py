from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Image(models.Model):
    title = models.CharField(max_length=250)
    ifile = models.ImageField(upload_to='photos')
    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='image_uploader')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100)