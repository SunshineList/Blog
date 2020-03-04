from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class UserToken(models.Model):
    username = models.OneToOneField(to='Info', on_delete=models.DO_NOTHING)
    token = models.CharField('token', max_length=60)

    class Meta:
        db_table = 'user_token'
        verbose_name = verbose_name_plural = '用户token表'


TYPE = (
    ('0', '管理员'),
    ('1', '普通用户')
)


class Info(models.Model):
    type = models.CharField('类型', choices=TYPE, null=True, blank=True, default='1', max_length=1)
    username = models.CharField('用户名', max_length=100, unique=True, null=True, blank=True)
    password = models.CharField('密码', max_length=100, null=True, blank=True)
    telphone = models.CharField('电话', max_length=20, null=True, blank=True)
    create_date = models.DateTimeField('注册日期', auto_now=True, null=True, blank=True)
    update_date = models.DateTimeField('更改日期', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '账号'

    def __str__(self):
        return self.username
