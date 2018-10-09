from django.db import transaction

from warehouse.models import Warehouse
from .serializers import DeviceSerializer, MessageSerializer, DeviceAttrSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from .models import Device, Message, DeviceAttr
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


# from rest_framework.response import Response
# Create your views here.


class DevicePagination(PageNumberPagination):
    # /?p=2&page_size=5
    page_size = 12
    page_size_query_param = 'page_size'  # 多少条
    page_query_param = "page"  # 多少页
    max_page_size = 100


class DeviceListView(viewsets.ModelViewSet):
    """
    Device list
    """

    permission_classes = (IsAdminUser,)
    pagination_class = DevicePagination
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('id', 'code', 'warehouse', 'status')
    ordering_fields = ('create_time', 'move_num')

    # lookup_field = "device_id"

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_superuser:
            return Device.objects.all()
        else:
            return Device.objects.filter(id=user.id)


class DeviceAttrView(viewsets.ModelViewSet):
    """
    Device operation
    """
    permission_classes = (IsAdminUser,)
    queryset = DeviceAttr.objects.all()
    serializer_class = DeviceAttrSerializer

    # lookup_field = "device_id"
    #
    # def perform_create(self, serializer):
    #     shop_cart = serializer.save()
    #     devices = devices_cart.devices
    #     devices.devices_num -= devices_cart.nums
    #     devices.save()


class MessageView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Message list
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


class DeviceOperation(APIView):
    def get(self, request):

        return Response("success")

    def post(self, request):
        device_ids = request.POST.getlist("device_id")
        action = request.POST.get('active')
        warehouse_id = request.POST.get("warehouse")
        user = self.request.user

        if action == "出库":
            # 必须是入库的
            for device_id in device_ids:
                device = Device.objects.filter(id=device_id, warehouse=warehouse_id, status=1).first()
                if device:
                    try:
                        with transaction.atomic():
                            device.state = 0
                            device.out_num += 1  # 出库次数
                            # device.move_num += 1  # 流转数量
                            Message.objects.create(
                                do_type=action,
                                user_id=user.id,
                                warehouse_id=warehouse_id,
                                device_id=device_id,
                                use_num=len(device_ids),
                            )
                            device.save()
                        return Response('success')
                    except Exception as e:
                        print(e)
                        return Response("操作失败")
                else:
                    return Response("该设备不存在或该设备无法被出库")

        if action == "入库":
            # 出库或调拨的
            for device_id in device_ids:
                device = Device.objects.filter(id=device_id, warehouse=warehouse_id, status__in=(0, 2)).first()
                if device:
                    try:
                        with transaction.atomic():
                            device.state = 1
                            device.in_num += 1
                            device.use_num += 1  # 使用寿命
                            Message.objects.create(
                                do_type=action,
                                user_id=user.id,
                                warehouse_id=warehouse_id,
                                device_id=device_id,
                                use_num=len(device_ids),
                            )
                            device.save()
                        return Response("success")
                    except Exception as e:
                        print(e)
                        return Response("操作失败")
                else:
                    return Response("该设备不存在或该设备无法被入库")

        if action == "调拨":
            for device_id in device_ids:
                # 必须是入库的
                device = Device.objects.filter(id=device_id, warehouse=warehouse_id, status__in=(0, 2)).first()
                if device:
                    aim_warehouse_id = request.POST.get("aim_warehouse")
                    if Warehouse.objects.filter(id=aim_warehouse_id):
                        try:
                            with transaction.atomic():
                                device.warehouse = aim_warehouse_id
                                device.state = 2
                                device.out_num += 1
                                Message.objects.create(
                                    do_type=action,
                                    user_id=user.id,
                                    warehouse_id=warehouse_id,
                                    device_id=device_id,
                                    use_num=len(device_ids),
                                )
                                device.save()
                            return Response("success")
                        except Exception as e:
                            print(e)
                            return Response("操作失败")
                    else:
                        return Response("不存在该仓库")
                else:
                    return Response("该设备不存在或该设备无法被调拨")

        if action == "报废":
            for device_id in device_ids:
                device = Device.objects.filter(id=device_id, warehouse=warehouse_id).first()
                if device:
                    try:
                        with transaction.atomic():
                            device.state = 3
                            device.out_num += 1
                            Message.objects.create(
                                do_type=action,
                                user_id=user.id,
                                warehouse_id=warehouse_id,
                                device_id=device_id,
                                move_num=len(device_ids),
                            )
                            device.save()
                        return Response("success")
                    except Exception as e:
                        print(e)
                        return Response("操作失败")
                else:
                    return Response("设备不存在")
