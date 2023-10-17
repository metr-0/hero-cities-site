from django.db import models


class CityManager(models.Manager):
    def points(self):
        return [
            {
                'id': city.id,
                'name': city.name,
                'x': float(city.lantitude),
                'y': float(city.longtitude),

            } for city in self.get_queryset()

        ]


class City(models.Model):
    objects = CityManager()

    name = models.CharField(
        verbose_name="Название",
        max_length=255,
    )

    annotation = models.CharField(
        verbose_name="Аннотация",
        max_length=255,
        null=True
    )

    text = models.TextField(
        verbose_name="Описание",
        null=True,
    )

    old_image = models.ImageField(
        verbose_name='Историческое изображение',
        null=True
    )

    new_image = models.ImageField(
        verbose_name='Современное изображение',
        null=True
    )

    lantitude = models.DecimalField(
        verbose_name="Широта",
        max_digits=22,
        decimal_places=16,
    )

    longtitude = models.DecimalField(
        verbose_name="Долгота",
        max_digits=22,
        decimal_places=16,
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
