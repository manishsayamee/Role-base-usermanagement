from django.urls import path
from .views import SignupView, SignupmakerView, SignupCheckerView,login_View, logout_view
#  SignupmakerView, SignupcheckerView, login

app_name='accounts'
urlpatterns=[
  # accounts/signup/
  path('signup/', SignupView.as_view(), name='signup'),
  path('maker/',SignupmakerView.as_view(), name='signupmaker'),
  path('checker/',SignupCheckerView.as_view(), name='signupchecker'),
  path('login/', login_View, name='login'),
  path('logout/', logout_view, name='logout'),



]