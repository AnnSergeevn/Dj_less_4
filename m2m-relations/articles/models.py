from django.db import models



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Articles_tag(models.Model):
    name = models.TextField(verbose_name='Название')
    articles = models.ManyToManyField(Article, related_name="articles_tag", through="Articles_scope")


class Articles_scope(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="scopes")
    tag = models.ForeignKey(Articles_tag, on_delete=models.CASCADE, related_name="scopes")

    is_main = models.BooleanField()

