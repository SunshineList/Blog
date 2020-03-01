from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
