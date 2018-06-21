"""用户页面url"""

from django.urls import path
from  robot.views import wechat_API
urlpatterns = [
   path(r'weChat/', wechat_API.home),
   path(r'get_access_token/', wechat_API.get_access_token),
]