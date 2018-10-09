from .models import Warehouse
from .serializers import WarehouseSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.


class WarehouseListView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated, )
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('id', 'city', 'user', 'create_time')
    ordering_fields = ('create_time', 'move_num')

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_superuser:
            return Warehouse.objects.all()
        else:
            return Warehouse.objects.filter(id=user.id)


