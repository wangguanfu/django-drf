"""iot_ruhr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from device.views import DeviceListView, MessageView, DeviceAttrView, DeviceOperation
from warehouse.views import WarehouseListView


router = DefaultRouter()

# 配置device的url
router.register(r'device', DeviceListView, base_name="device")
router.register(r'message', MessageView, base_name="message")

# 配置device的url
router.register(r'warehouse', WarehouseListView, base_name="warehouse")

# 配置device操作的url
# router.register(r'operation', DeviceAttrView, base_name="operation")


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # # drf自带的token认证模式
    # url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口 登录
    url(r'^login/', obtain_jwt_token),
    # 文档
    url(r'docs/', include_docs_urls(title='鲁尔api')),

    # url 配置
    url(r'^', include(router.urls)),
    url(r'^operation/', DeviceOperation.as_view(), name="operation")

]
