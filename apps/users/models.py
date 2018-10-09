from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel

# Create your models here.


class UserProfile(AbstractUser, BaseModel):
    """用户"""
    city = models.CharField(max_length=256, verbose_name="所在城市")

    class Meta:
        db_table = "ru_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    #  重写save方法
    def save(self, *args, **kwargs):
        self.is_staff = True
        super(UserProfile, self).save(*args, **kwargs)


class Address(BaseModel):
    """地址"""
    user = models.ForeignKey(UserProfile, verbose_name="所属用户")
    receiver_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    detail_addr = models.CharField(max_length=256, verbose_name="所在地")
    zip_code = models.CharField(max_length=6, verbose_name="邮政编码")

    class Meta:
        db_table = "ru_address"

