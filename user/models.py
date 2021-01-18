from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        user = self.model(username=username, **extra_fields)
        # Hash The Password using bcrypt using secret key as salt
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=300)
    # is_admin = models.BooleanField()
    username = models.TextField(unique=True,max_length=20)
    password = models.TextField()

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
