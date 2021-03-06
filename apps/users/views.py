# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
# from rest_framework.mixins import CreateModelMixin
# from rest_framework import mixins
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from random import choice
# from rest_framework import permissions
# from rest_framework import authentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#
# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
#
# from .serializers import UserDetailSerializer


User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#
# class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     用户
#     """
#
#     queryset = User.objects.all()
#     authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
#
#     def get_serializer_class(self):
#         if self.action == "retrieve":
#             return UserDetailSerializer
#         else:
#             return
#
#         return UserDetailSerializer
#
#
#     # permission_classes = (permissions.IsAuthenticated, )
#     def get_permissions(self):
#         if self.action == "retrieve":
#             return [permissions.IsAuthenticated()]
#         elif self.action == "create":
#             return []
#
#         return []
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_create(serializer)
#
#         re_dict = serializer.data
#         payload = jwt_payload_handler(user)
#         re_dict["token"] = jwt_encode_handler(payload)
#         re_dict["name"] = user.name if user.name else user.username
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
#
#     def get_object(self):
#         return self.request.user
#
#     def perform_create(self, serializer):
#         return serializer.save()




