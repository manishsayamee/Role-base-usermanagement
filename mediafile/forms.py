from django import forms
from .models import UploadFile, Comment

class FileCreateForm(forms.ModelForm):
  class Meta:
    model = UploadFile
    fields = [ 'title','file', 'Type']
  
  # def save(self):
  #   filedata = super().save(commit=False)
  #   filedatatype = self.cleaned_data['file']
  #   filename = filedatatype.name

  #   def checkfiletype():
  #     if filename.endswith('.pdf'):
  #       return 1
  #     elif filename.endswith('.png'):
  #       return 2
  #     else:
  #       return 3

  #   filedata.fileoffile = checkfiletype
  #   filedata.save()
  #   return filedata
    


class commentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name','body']


