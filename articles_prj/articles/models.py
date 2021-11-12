from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField('article name', max_length=200)
    text = models.TextField('article text')
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
        return self.title

    def IsRecent(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('author name', max_length = 50)
    comment_text = models.CharField('comment text', max_length = 350)

    def __str__(self):
        return f"comment by: {self.author_name}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
