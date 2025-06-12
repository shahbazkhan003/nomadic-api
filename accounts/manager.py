from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, fullname, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not fullname:
            raise ValueError("Users must have a full name")

        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password):
        user = self.create_user(email=email, fullname=fullname, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

