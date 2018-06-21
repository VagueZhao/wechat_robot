import urllib

from Crypto.SelfTest.Signature.test_dss import res
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import parse,request
from robot.services import wechatAPI_service

#微信公众号入口
@csrf_exempt
def home(request):
    rsp = wechatAPI_service.home(request)
    #request.session['user_info'] = rsp
    #print('___________________', request.session.get('user_info'))
    return HttpResponse(rsp)

#测试access_token获取
@csrf_exempt
def get_access_token(request):
    access_token = wechatAPI_service.get_access_token(request)
    print(access_token)
    return render(request, 'firstpage.html')
    #return True, HttpResponse(access_token)



