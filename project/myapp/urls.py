from django.conf.urls import url
from django.urls import path,re_path
from . import views


urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^(\d+)/$',views.detail),
    re_path(r'^grades/$',views.grades),
    re_path(r'^students/$',views.students),
    re_path(r'^students3/$', views.students3),
    re_path(r'^stu/(\d+)/$',views.stupage),
    re_path(r'^studentssearch/$', views.studentssearch),

    re_path(r'^grades/(\d+)/$',views.gradesstudents),
    re_path(r'^addstudent/$',views.addstudent),
    re_path(r'^addstudent1/$',views.addstudent1),
    re_path(r'^grades1/$',views.grades1),

    re_path(r'^attriblues/$',views.attriblues),
    re_path(r'^get1/$',views.get1),
    re_path(r'^get2/$',views.get2),

    re_path(r'^showregist/$',views.showregist),
    re_path(r'^showregist/regist/$', views.regist),

    re_path(r'^showresponse/$',views.showresponse),

    re_path(r'^cookietest/$',views.cookietest),
    re_path(r'^showcookie/$',views.showcookie),

    re_path(r'^redirect1/$', views.redirect1),
    re_path(r'^redirect2/$', views.redirect2),

    re_path(r'^main/$',views.main),
    re_path(r'^login/$',views.login),
    re_path(r'^showmain/$',views.showmain),
    re_path(r'^quit/$',views.quit),



]