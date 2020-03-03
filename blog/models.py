from django.db import models
from account.models import Info


class Article(models.Model):
    author = models.ForeignKey(Info, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField('标题', max_length=32)
    content = models.TextField('内容', null=True)
    pub_time = models.DateTimeField('发布日期', auto_now_add=True, null=True)

    def __str__(self):
        return self.title
