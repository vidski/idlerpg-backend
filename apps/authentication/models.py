from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # created_at = models.DateTimeField("created at", auto_now_add=True)
    # modified_at = models.DateTimeField("modified at", auto_now=True)

    def __str__(self):
        return self.email if self.email else self.username