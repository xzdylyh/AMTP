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
from amt import views_user
from amt import views_login
from amt import views_case
from amt import views_run

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),

    url(r'^login_ajax/$',views_login.login_ajax),
    url(r'^login_validation/$',views_login.login_validation),
    url(r'^$',views_login.login_ajax,name='login_ajax'),
    url(r'^logout/$',views_login.logout),
    url(r'^reset_secret/$',views_login.reset_secret),
    url(r'^reset_password/$',views_login.reset_password),

    url(r'^user_register/$',views_user.user_register),
    url(r'^register/$',views_user.register),


    url(r'^case_add_data/$',views_case.case_add_data),
    url(r'^case_delete_data/$',views_case.case_delete_data),
    url(r'^case_modify_data/$',views_case.case_modify_data),
    url(r'^select_case_data/$',views_case.select_case_data),
    url(r'^iface/$',views_case.case_manage_iface),
    url(r'^scenario_manage/$',views.scenario_manage),

    url(r'^system/$',views.system),

    url(r'^run_test/$',views_run.run_test),
]
