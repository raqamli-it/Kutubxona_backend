from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
