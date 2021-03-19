from django.db import models
from django.urls import reverse

from .utils import generate_slug


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
        verbose_name="URL-slug", max_length=255, null=True, blank=True
    )

    def generate_slug(self, title=None):
        if not title:
            title = self.title
        unique_slug = generate_slug(title)
        num = 1
        while (
            self.__class__.objects.filter(slug=unique_slug)
            .exclude(pk=self.pk)
            .exists()
        ):
            unique_slug = "{}-{}".format(unique_slug, num)
            num += 1

        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # TODO: fix class reverse
        return reverse(
            "{}-detail".format(self.__class__.lower()),
            kwargs={"slug": self.slug},
        )

    class Meta:
        abstract = True
