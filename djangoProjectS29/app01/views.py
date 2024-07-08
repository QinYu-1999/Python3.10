import random
import json
from django.shortcuts import render,HttpResponse
from djangoProjectS29.Utils.Tencent.sms import send_sms_single


def send_sms(request):
    code = random.randrange(1000, 9999)
    res = send_sms_single('17722754206', 2176140, [code, ])
    print(res)
    return HttpResponse('成功')