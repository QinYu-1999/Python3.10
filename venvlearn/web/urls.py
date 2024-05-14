# from django.shortcuts import HttpResponse
from django.urls import path
from web import views

urlpatterns=[
    #web/Home
    path('Home/',views.home),
    path('requestLearn/',views.requestLearn,name = 'requestlearn'),
    path('jsonlearn/',views.jsonlearn,name = 'jsonlearn'),
]