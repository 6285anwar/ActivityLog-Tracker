"""activitylog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from activityapp import views
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin Section 
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^admin_logout/$', views.admin_logout,name='admin_logout'),
    re_path(r'^admin_index/$', views.admin_index, name='admin_index'),
    re_path(r'^admin_dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    re_path(r'^admin_addsalesman/$', views.admin_addsalesman, name='admin_addsalesman'),
    re_path(r'^admin_useractivity/$', views.admin_useractivity, name='admin_useractivity'),
    re_path(r'^admin_userprofile/(?P<id>\d+)/$', views.admin_userprofile, name='admin_userprofile'),
    

    #user Section
    re_path(r'^user_logout/$', views.user_logout,name='user_logout'),
    re_path(r'^user_index/$', views.user_index, name='user_index'),
    re_path(r'^user_dashboard/$', views.user_dashboard, name='user_dashboard'),
    re_path(r'^user_addactivity/$', views.user_addactivity, name='user_addactivity'),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

