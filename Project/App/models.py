from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  header_image = models.ImageField(null=True, blank=True, upload_to='images/')
  slug =   models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  #picture= models.ImageField(upload_to=settings.MEDIA_ROOT, default='/static/img/default.png')
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-updated_on','-created_on']

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("home")

class Comment(models.Model):
  post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s - %s' % (self.post.title, self.name)