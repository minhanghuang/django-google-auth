from django.db import models

# Create your models here.

class DjangoGoogleAuthenticator2(models.Model):

    username = models.CharField(
        verbose_name="用户名",
        max_length=255,
    )

    key = models.CharField(
        verbose_name="秘钥",
        max_length=255,
        unique=True,
    )

    class Meta:
        db_table = 'google_authenticator2'



