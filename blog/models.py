from django.db import models


class Article(models.Model):
    author = models.CharField("发布人", max_length=50, null=True, blank=True)
    title = models.CharField('标题', max_length=32)
    content = models.TextField('内容', null=True)
    pub_time = models.DateTimeField('发布日期', auto_now_add=True, null=True)

    def __str__(self):
        return self.title
