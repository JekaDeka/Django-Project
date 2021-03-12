from django.db import models
from django.urls import reverse

from .utils import transliterate


class Displayable(models.Model):
    DRAFT = "AB"
    PUBLISHED = "PB"

    STATUS_CHOICES = [
        (DRAFT, "Черновик"),
        (PUBLISHED, "Опубликовано"),
    ]

    status = models.CharField(
        verbose_name="Статус записи",
        max_length=2,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    def publish(self):
        self.status = self.PUBLISHED
        self.save()

    class Meta:
        abstract = True


class Slugged(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    slug = models.CharField(
        verbose_name="URL-slug", unique=True, max_length=255
    )

    def generate_slug(self, title=None):
        if not title:
            title = self.title
        # Мое новое кулинарное шоу => Moe_novoe_kulinarnoe_shoy
        # 1. Попытаться получить существующую модель с таким slug
        # 2. Если такого объекта нет, то все ок.
        # => title => translit/remove whistespace => slug
        # 3. Если объект с таким slug существует, то:
        # => title + .... (random A-Z0-9) =>
        # translit / remove whistespace => slug
        slug = transliterate(title)
        return slug

    def get_absolute_url(self):
        return reverse(
            "{}-detail".format(self.__class__.lower()),
            kwargs={"slug": self.slug},
        )

    class Meta:
        abstract = True
