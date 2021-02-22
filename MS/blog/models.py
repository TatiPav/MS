from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#
#
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

        # return super().get_queryset().filter(status='Опубликовано')
        # return super(PublishedManager, self).get_queryset().filter(status='published')
#
# 1. Определяем модель Post
class Post(models.Model):
    # выбор статуса
    STATUS_CHOICES = (
        # ('draft', 'Draft'),
        # ('published', 'Published'),

        ('draft', 'Проект'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField('Наименование', max_length=250)
    slug = models.SlugField('Путь', max_length=250,
                            unique_for_date='publish')

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='blog_posts')

    body = models.TextField('Содержание')
    publish = models.DateTimeField('Дата публикации', default=timezone.now)
    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    status = models.CharField('Статус', max_length=20,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()  # Менеджер по умолчанию..
    published = PublishedManager()  # Наш новый менеджер..

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
