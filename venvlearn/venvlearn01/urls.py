"""venvlearn01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from web import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #web/
    path('web/', include('web.urls')),
    # path('admin/', admin.site.urls),
    path('Home/',views.home,name='v1'),
    # path('News/<int:nid>/',views.news),
    # path('Aritc/',views.Aritc)
    path('logon/<str:role>/',views.logon,name='v3'),
    re_path(r'auth/(\d+)/(\w+)',views.auth,name='v4'),
    re_path(r'auth/(?P<nid>\d+)/(?P<name>\w+)', views.auth, name='v5'),
    # path("requestLearn/",include('web.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
