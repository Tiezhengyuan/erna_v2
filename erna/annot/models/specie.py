from django.db import models


class Specie(models.Model):
    specie_name = models.CharField(max_length=256, unique=True)
    abbreviation = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    scientific_name = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )

    class Meta:
        app_label = 'annot'
        ordering = ['specie_name',]

    def __str__(self):
         return self.specie_name