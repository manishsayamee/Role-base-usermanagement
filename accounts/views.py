from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
from .models import User
from .forms import SignupmakerForm, SignupCheckerForm
from .forms import loginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import get_user_model

USER = get_user_model()
class SignupView(TemplateView):
  template_name = 'accounts/home.html'


class SignupmakerView(CreateView):
  form_class = SignupmakerForm
  template_name = 'accounts/makersignup.html'
  success_url = '/accounts/login'


class SignupCheckerView(CreateView):
  form_class = SignupCheckerForm
  template_name = 'accounts/checkersignup.html'
  success_url = '/accounts/login'




def login_View(request):
  if request.method == 'POST':
    form = loginForm(request.POST)
    if form.is_valid():
      user = authenticate(username = form.cleaned_data['username'],
                          password = form.cleaned_data['password'])
      if user:
        print("User is found")
        login(request,user)
        return redirect('/files/list')

      else:
        print("User isnot found")
  elif request.method == 'GET':
    form = loginForm()
  return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
  logout(request)
  return redirect('/accounts/login')