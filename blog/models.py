from django.db import models

NULLABLE = {'blank': True, 'null': True}
class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    date = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}, дата публикации {self.date}'

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"