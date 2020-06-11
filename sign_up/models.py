from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
