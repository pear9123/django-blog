from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager

DEFAULT = 'user/ben.jpg'

class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(gender=self.model.GENDER_OTHER, *args, **kwargs)

class User(AbstractUser):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
        (GENDER_OTHER, '기타'),
    )
    img_profile = models.ImageField(upload_to='user', blank=True, default=DEFAULT)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)

    objects = UserManager()

    def set_image_to_default(self):
        self.img_profile.delete(save=False)
        self.img_profile = DEFAULT
        self.save()

    def __str__(self):
        return self.username
