from rest_framework import serializers
from django.db.models import Q
from .models import Device, Message, DeviceAttr
from warehouse.models import Warehouse
from users.models import UserProfile


class DeviceAttrSerializer(serializers.Serializer):
    # user = serializers.HiddenField(
    #         default=serializers.CurrentUserDefault()
    #     )
    # # number = serializers.IntegerField(required=True, label="总数量")
    # move_num = serializers.IntegerField(required=True, label="流动数量")
    # type = serializers.CharField(max_length=100, label="类型")
    # # warehouse = serializers.PrimaryKeyRelatedField(required=True, queryset=Device.objects.all(), label="所在仓库")

    class Meta:
        model = DeviceAttr
        fields = ('type', 'move_num')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer()
    device_attr = DeviceAttrSerializer()

    class Meta:
        model = Device
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer()
    user = UserProfileSerializer()
    device = DeviceSerializer()

    class Meta:
        model = Message
        fields = "__all__"


# class DeviceOperationSerializer(serializers.Serializer):
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     status = serializers.ChoiceField(required=True, label="设备状态", choices=((0, "出库"),
#                                                                             (1, "入库"),
#                                                                             (2, "调拨"),
#                                                                             (3, "报废"),),
#                                       # error_messages={
#                                       #     # "min_value": "商品数量不能小于一",
#                                       #     # "required": "请选择购买数量"}
#                                       )
#     move_num = serializers.IntegerField(required=True, label="流动数量")
#     name = serializers.CharField(required=True, label="名称")
#     # destination = serializers.PrimaryKeyRelatedField(required=True, queryset=Device.objects.all(), label="目的仓库")
#     warehouse = serializers.PrimaryKeyRelatedField(required=True, queryset=Device.objects.all(), label="所在仓库")
#     code = serializers.CharField(required=True, label="编码")
#
#     # class Meta:
#     #     model = Device
#     #     fields = ('type', 'do_type')
#
#     .context["request"].user
#         nums = vadef create(self, validated_data):
#         user = selflidated_data["number"]
#
#         existed = Device.objects.filter(user=user, id=user.id)
#
#         if existed:
#             existed = existed[0]
#             existed.nums += nums
#             existed.save()
#         else:
#             existed = Device.objects.create(**validated_data)
#
#         return existed
#
#     def update(self, instance, validated_data):
#         # 修改数量
#         instance.number += validated_data["number"]
#         instance.save()
#         return instance






















