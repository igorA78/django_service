from django.db import models

from main.models import NULLABLE


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    published_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
