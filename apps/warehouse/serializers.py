from rest_framework import serializers
from django.db.models import Q

from .models import Warehouse
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Warehouse
        fields = "__all__"

