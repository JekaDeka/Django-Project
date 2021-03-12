from django.conf import settings
from django.db import models
from generic.models import Displayable, Slugged


class BlogAuthor(Slugged):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    bio = models.TextField(max_length=1000)
    vk = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "Автор блога"
        verbose_name_plural = "Авторы блога"


class BlogCategory(Slugged):
    class Meta:
        verbose_name = "Категория блога"
        verbose_name_plural = "Категории блога"


class BlogPost(Slugged, Displayable):
    content = models.TextField(verbose_name="Содержимое")
    category = models.ForeignKey(
        BlogCategory,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
    )
    author = models.ForeignKey(
        BlogAuthor,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"
