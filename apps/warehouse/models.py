from django.db import models
from utils.models import BaseModel
from users.models import UserProfile
# Create your models here.


class Warehouse(BaseModel):
    """仓库"""

    name = models.CharField(max_length=20, verbose_name="仓库名称")
    type = models.CharField(max_length=20, blank=True, null=True,  verbose_name="仓库类型")
    city = models.CharField(max_length=100, verbose_name="城市")  # 库区
    now_num = models.IntegerField(default=0, verbose_name="当前库存")
    total = models.IntegerField(default=0, verbose_name="总数量")
    user = models.ForeignKey(UserProfile, verbose_name="所属用户")

    class Meta:
        verbose_name = "仓库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_code(self):
        code = self.device_set.all().first()
        return code

    get_code.short_description = '编码'

    def get_type(self):
        types = self.device_set.all().values("device_attr__type").first()
        for type in types.values():
            return type

    get_type.short_description = '型号'






































