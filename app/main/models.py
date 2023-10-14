from django.db import models


class City(models.Model):
    name = models.CharField(
        verbose_name="название",
        max_length=49,
        blank=False,
        null=False,
    )

    text = models.TextField(
        verbose_name="описание",
    )

    lantitude = models.DecimalField(
        verbose_name="широта",
        max_digits=22,
        decimal_places=16,
    )

    longtitude = models.DecimalField(
        verbose_name="долгота",
        max_digits=22,
        decimal_places=16,
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

