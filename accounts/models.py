from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  is_maker = models.BooleanField(default=False)
  is_checker = models.BooleanField(default=False)
  confirm_password = models.CharField(max_length=120, blank=True)
  # confirm_password set blank because i have already create a database and it ask to set default value so
