from django.db import models
from utils.models import BaseModel
from warehouse.models import Warehouse
from users.models import UserProfile
# Create your models here.


class DeviceAttr(BaseModel):
    """
    保温箱类型
    """
    type = models.CharField(max_length=100, verbose_name="型号")
    # move_num = models.IntegerField(default=0, verbose_name="流转数量")
    number = models.IntegerField(default=0, verbose_name="总数量")
    desc = models.CharField(max_length=100, blank=True, null=True, verbose_name="描述")
    destination = models.CharField(max_length=20, blank=True, null=True, verbose_name="目的仓库")

    class Meta:
        verbose_name = "保温箱类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type


class Device(BaseModel):
    """
    保温箱设备
    """
    DO_TYPE_CHOICES = (
        (0, "出库"),
        (1, "入库"),
        (2, "调拨"),
        (3, "报废"),
    )
    name = models.CharField(max_length=20, verbose_name="名称")  # unique=True
    # type = models.CharField(max_length=100, verbose_name="类型")
    code = models.CharField(max_length=100, verbose_name="编码")
    status = models.SmallIntegerField(choices=DO_TYPE_CHOICES, blank=True, null=True, verbose_name="设备状态")

    out_num = models.IntegerField(default=0, verbose_name="出库次数")
    in_num = models.IntegerField(default=0, verbose_name="入库次数")
    life = models.IntegerField(default=400, verbose_name="寿命时长")
    use_num = models.IntegerField(default=0, verbose_name="使用寿命")

    device_attr = models.ForeignKey(DeviceAttr, blank=True, null=True, verbose_name="设备类型")
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, verbose_name="所属仓库")
    # is_destroy = models.BooleanField(default=0, verbose_name="是否报废")

    class Meta:
        verbose_name = "保温箱设备"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Message(BaseModel):
    """
    操作信息
    """
    do_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="操作动作")
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, verbose_name="仓库")
    device = models.ForeignKey(Device, blank=True, null=True, verbose_name="设备")
    user = models.ForeignKey(UserProfile, blank=True, null=True, verbose_name="用户")
    move_num = models.IntegerField(default=0, verbose_name="流转数量")
    # time = models.CharField(max_length=20, verbose_name="操作时间")

    class Meta:
        verbose_name = "操作信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

    def get_user(self):
        pass


































