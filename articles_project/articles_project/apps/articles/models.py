from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField('название статьи', max_length=200)
    text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('время публикации')

    def __str__(self):
        return self.title

    def IsRecent(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 350)

    def __str__(self):
        return f"comment by: {self.author_name}"
