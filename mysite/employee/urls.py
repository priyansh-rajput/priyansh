__author__ = 'priyansh'
from django.conf.urls import patterns,url
from employee import views
urlpatterns=patterns('',url(r'^$',views.registration,name='registration'),
                     url(r'^/employeeInsert/$',views.employeeInsert,name='employeeInsert'),
                     url(r'^/emloyeeLogin/$',views.employeeLogin,name='employeeLogin'),
                     url(r'^/moveLogin/$',views.moveLogin,name='moveLogin'),
                     url(r'^/moveforgotPassword/$',views.moveForgotPassword,name='moveforgotPassword'),
                     url(r'^/forgotPassword/$',views.forgotPassword,name='forgotPassword'),
                     url(r'^/logout/$',views.logout,name='logout'),
                     url(r'^/moveLogout/$',views.moveLogout,name='moveLogout'),

)