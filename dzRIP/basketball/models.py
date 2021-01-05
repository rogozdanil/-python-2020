from django.db import models
from datetime import date
from django.urls import reverse

class Player(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    height = models.PositiveSmallIntegerField("Рост", default=0)
    weight = models.PositiveSmallIntegerField("Вес", default=0)
    points = models.PositiveSmallIntegerField("Кол-во очков", default=0)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"


class Commands(models.Model):
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Винрейт", max_length=20, default='')
    description = models.TextField("Описание")
    commands = models.ManyToManyField(Player, verbose_name="игроки", related_name="name_commands")


    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("commands_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Команды"
        verbose_name_plural = "Команды"
# Create your models here.
