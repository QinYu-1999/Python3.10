from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMd1(MiddlewareMixin):
    # 先执行
    def process_request(self, request):
        print('md1来了')
        # return HttpResponse('nn')

    # 后执行
    def process_response(self, request, response):
        print('md1走了')
        return response


class MyMd2(MiddlewareMixin):
    # 先执行
    def process_request(self, request):
        print('md2来了')
        # return HttpResponse('nn')

    # 后执行
    def process_response(self, request, response):
        print('md2走了')
        return response

class MyMd3(MiddlewareMixin):
        # 先执行
        def process_request(self, request):
            print('md3来了')
            # return HttpResponse('nn')

        # 后执行
        def process_response(self, request, response):
            print('md3走了')
            return response
