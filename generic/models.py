from django.db import models
from django.urls import reverse

from .utils import transliterate
from .utils import slugify


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

        unique_slug = transliterate(title)
        num = 1
        while Slugged.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1       

        return unique_slug

    def get_absolute_url(self):
        return reverse(
            "{}-detail".format(self.__class__.lower()),
            kwargs={"slug": self.slug},
        )

    class Meta:
        abstract = True
