import xadmin
from xadmin import views
from .models import Device, Message, DeviceAttr


class DeviceAdmin(object):

    list_display = ['name', 'status', 'code', 'out_num', 'in_num', 'life', 'warehouse', 'create_time']
    search_fields = ['name', 'code']
    list_filter = ['name', 'code', 'status']
    # ordering = ['-number']


class DeviceAttrAdmin(object):

    list_display = ['type', 'move_num', 'number']
    search_fields = ['type', 'move_num', 'number']
    list_filter = ['type', 'move_num', 'number']
    # ordering = ['-number']


class MessageAdmin(object):

    list_display = ['warehouse', 'device', 'user', 'do_type']
    # search_fields = ['name', 'time', 'city', 'code']
    # list_filter = ['name', 'type', 'city', 'code']
    # ordering = ['-number']


xadmin.site.register(Device, DeviceAdmin)
xadmin.site.register(DeviceAttr, DeviceAttrAdmin)
xadmin.site.register(Message, MessageAdmin)