from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class AuthorUser(AbstractUser):
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    # name = models.CharField(max_length=200, verbose_name="ФИО")
    # dep_editor = models.CharField(
    #     max_length=200, verbose_name="Редактор отдела")
    # email = models.EmailField(verbose_name="Почта автора")

    # def __str__(self):
    #     return self.name


class Article(models.Model):
    heading = models.CharField(max_length=150, verbose_name="Заголовок статьи")
    description = models.TextField(verbose_name="Описание статьи")
    art_type = models.CharField(
        max_length=100, verbose_name="Тип публикации статьи (Закрытый/Открытый)")
    author = models.ForeignKey(AuthorUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('index')
