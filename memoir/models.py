from django.db import models
from django.db import models
from .helpers import *
from django.contrib.auth.models import User



# Create your models here.

from froala_editor.fields import FroalaField


class Profile(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images/blogs/profile")




class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True ,null=True ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.title

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

