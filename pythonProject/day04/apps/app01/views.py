import datetime

from django.shortcuts import render, HttpResponse
from apps.app01 import models
from apps.app02 import models as m2


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return 'sjsjsj'


def index(request):
    # pass
    context = {
        "n1": "123",
        "n2": [123, 2],
        "n3": {
            "name": "able",
            "age": 99
        },
        "n4": Person("Able", 23),
        'n5': 'zhangwen',
        'n6': datetime.datetime.now(),
        'n7': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    return render(request, 'app01/index.html', context)
    # return render(request,'app01/index.html')


def home(request):
    print('函数')
    return render(request, 'app01/home.html')


def _sql(request):
    # 创建
    # v1 = models.UserInfo.objects.using('default').create(name='Able', age=21)
    # v1 = models.UserInfo.objects.create(name='skks', age=15)
    #  读取
    v2 = models.UserInfo.objects.all()
    print(v2.query)
    # obj = models.UserInfo.objects.create(name = 'aaa',age=11)
    # print(obj,obj.name,obj.ct_date)
    obj = models.UserInfo(name='aaa1', age=2)  #先放进内存  save()后才可以保存进数据库
    obj.age = 20
    # obj.save()
    # print(obj.query)
    return HttpResponse('返回')
