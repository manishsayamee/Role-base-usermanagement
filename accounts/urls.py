from django.urls import path
from .views import SignupView, SignupmakerView, SignupCheckerView,login_View, logout_view

app_name='accounts'
urlpatterns=[
  # accounts/signup/
  path('home/', SignupView.as_view(), name='home'),
  path('maker/',SignupmakerView.as_view(), name='signupmaker'),
  path('checker/',SignupCheckerView.as_view(), name='signupchecker'),
  path('login/', login_View, name='login'),
  path('logout/', logout_view, name='logout'),



]