from django.db import models
from accounts.models import User
import os 

class UploadFile(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=150)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  file = models.FileField()

  class Meta:
    ordering = ['-created_on']



  def css_class(self):
    extension = os.path.splitext(self.file.name)
    if extension == 'pdf':
      return 'pdf'
    elif extension == 'doc':
      return 'word'
    elif extension == 'png':
      return 'png'
    else:
      return 'mp4'



class Comment(models.Model):
  mediafile = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=150, blank=True)
  body = models.TextField()
  
  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)