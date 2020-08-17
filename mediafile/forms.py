from django import forms
from .models import UploadFile, Comment

class FileCreateForm(forms.ModelForm):
  class Meta:
    model = UploadFile
    fields = [ 'title','file']



class commentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name','body']


