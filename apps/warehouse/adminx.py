import xadmin

from .models import Warehouse
#
# class Warehouseline(object):
#     model = Warehouse
#     extra = 0


class WarehouseAdmin(object):
    list_display = ['get_code', 'get_type', 'name', 'city', 'now_num', 'user']
    search_fields = ['name', 'city', 'now_num']
    list_filter = ['name', 'city', 'now_num']
    ordering = ['-now_num']

    # readonly_fields = ['number', ]
    # exclude = ['number', ]
    # # inlines = ['WarehouseAdmin', ]
    # list_editable = ['type', 'number']
    # # refresh_times = [3,5]
    # # style_fields = {'detail':'ueditor'}

    # def save_models(self):
    #     # 在保存仓库的时候统计设备数量
    #     obj = self.new_obj
    #     obj.save()
    #     if obj.number is not None:
    #         number = obj.number
    #         number.device_nums = Warehouse.objects.filter(number=number).count()
    #         number.save()


xadmin.site.register(Warehouse, WarehouseAdmin)