from django import forms
from .models import User

class SignupmakerForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['first_name', 'last_name','username', 'email', 'password', 'confirm_password']

  def clean_username(self):
    if User.objects.filter(username=self.cleaned_data['username']).exists():
      raise forms.ValidationError("Username is already taken")
    return self.cleaned_data['username']

  def clean(self):
    password = self.cleaned_data['password']
    confirm_password = self.cleaned_data['confirm_password']
    if password != confirm_password:
      raise forms.ValidationError("Your password doesnot match!!")

  
  def save(self):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.is_maker = True
    user.save()
    return user

class SignupCheckerForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name','username', 'email', 'password', 'confirm_password']

  def clean_username(self):
    if User.objects.filter(username=self.cleaned_data['username']).exists():
      raise forms.ValidationError("Username is already taken")
    return self.cleaned_data['username']

  def clean(self):
    password = self.cleaned_data['password']
    confirm_password = self.cleaned_data['confirm_password']
    if password != confirm_password:
      raise forms.ValidationError("Your password doesnot match!!")

  
  def save(self):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.is_checker = True
    user.save()
    return user

class loginForm(forms.Form):
  username = forms.CharField(max_length=120)
  password = forms.CharField(max_length=120, widget=forms.PasswordInput())
  