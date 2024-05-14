from django.shortcuts import render,redirect,reverse
from django.shortcuts import HttpResponse
from django.http import JsonResponse
# Create your views here.
def home(request):
    return HttpResponse('首页')

def news(request,nid):
    print(nid)
    return HttpResponse('新闻')
def Aritc(request):
    page = request.GET.get("page")
    print(page)
    return HttpResponse("Aritc")
def logon(request,role):
    print("Logon")
    # return redirect('/Home/')
    #通过reverse 生成相对应的URL /Home/
    # url = reverse("v4")
    # print(url)
    # return redirect(url)
    #反向生成正则URL
    url = reverse('v3',kwargs={"role":"hhhhh"})
    print(url)
    url = reverse('v4', args=(666, 'wuua'))
    print(url)
    url = reverse('v5',kwargs={"nid":666,"name":"ssss"})
    print(url)
    return HttpResponse("logon")

def auth(request,nid,name):
    print('auth')
    return HttpResponse("auth")

def requestLearn(request):

    # 1.获取当前URL
    print(request.path_info)
    #2.URL传递的参数
    print(request.GET)
    print(request.GET.get('age'))
    #3.请求的方式
    print(request.method)

    #4.如果是POST请求，传递请求体(最原始数据)
    print(request.body)
    #4.1.请求头+请求体 b'v1=123&v2='1213'' content-Type = application/x-www-form-urlencoded   满足上述才会去解析进POST
    print(request.POST)
    print(request.POST.get('v1'))

    #4.2请求体+请求头  文件
    print(request.FILES) #文件格式内容  +multipart/form-data
    #5.1请求头
    print(request.headers)
    # 5.2cookies
    print(request.COOKIES)
    return HttpResponse("requestLearn")

def jsonlearn(request):
    print(request.method)

    # 返回JSON格式的数据
    # data_dict={"status":True,'data':[11,22,33]}
    # return JsonResponse(data_dict)

    # 重定向
    # return redirect('https://www.baidu.com')
    # return redirect('requestlearn')
    # url = reverse('requestlearn')
    # # print(url)
    # return redirect(url)

    # 渲染
    # - a.找到 'login.html' 并读取的内容，问题：去哪里找？
    # -   默认先去settings.TEMPLATES.DIRS指定的路径找。（公共）
    # -   按注册顺序每个已注册的app中找他templates目录，去这个目录中寻找'login.html'
    # -   一般情况下，原则，那个app中的的模板，去哪个那个app中寻找。
    # - b.渲染（替换）得到替换完成的字符串
    # - c.返回浏览器
    # return render(request,'login.html')

    # 响应头
    res = HttpResponse('login')
    res['xxx'] = 123
    return res