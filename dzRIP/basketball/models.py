from django.db import models


def player_photo(instance, filename):
    return 'players/{}/{}'.format(instance.pk, filename)


class Player(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    photo = models.ImageField(upload_to=player_photo, default='players/default.jpeg', verbose_name="Фото")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", default=0)
    height = models.PositiveSmallIntegerField(verbose_name="Рост", default=0)
    weight = models.PositiveSmallIntegerField(verbose_name="Вес", default=0)
    points = models.PositiveSmallIntegerField(verbose_name="Кол-во очков", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"


def commands_photo(instance, filename):
    return 'commands/{}/{}'.format(instance.pk, filename)


class Commands(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    stadium = models.CharField(verbose_name="Стадион", default="чикаго", max_length=100)
    winers = models.PositiveSmallIntegerField(verbose_name="Чемпионство", default=0)
    photo = models.ImageField(upload_to=commands_photo, default='commands/default.jpg', verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")
    players = models.ManyToManyField(Player, verbose_name="игроки", related_name="name_commands")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Команды"
        verbose_name_plural = "Команды"
