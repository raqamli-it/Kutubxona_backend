from django.db import models

from apps.shared.models import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Language(AbstractBaseModel):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Til'
        verbose_name_plural = 'Tillar'


class Book(AbstractBaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    scan = models.BooleanField(default=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'


class Discuss(AbstractBaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Muhokama'
        verbose_name_plural = 'Muhokamalar'


class Magazine(AbstractBaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = 'Jurnallar'


class Abstract(AbstractBaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Avtoreferat'
        verbose_name_plural = 'Avtoreferatlar'
