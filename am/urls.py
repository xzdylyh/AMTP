"""am URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from amt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^iface/$',views.case_manage_iface),
    url(r'^scenario_manage/$',views.scenario_manage),
    url(r'^login_ajax/$',views.login_ajax),
    url(r'^login_validation/$',views.login_validation),
    url(r'^$',views.login_ajax,name='login_ajax'),
    url(r'^base_page/$',views.base_page),
    url(r'^case_add_data/$',views.case_add_data),
    url(r'^case_delete_data/$',views.case_delete_data),
    url(r'^case_modify_data/$',views.case_modify_data),
    url(r'^select_case_data/$',views.select_case_data),
]
