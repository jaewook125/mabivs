from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.shortcuts import redirect
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login',
        kwargs={
            'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_ok/', TemplateView.as_view(template_name='accounts/signup_ok.html'), name='signup_ok'),
    url(r'^mypage/', views.mypage, name='mypage'),
    url(r'^user_list/', views.user_list, name='user_list'),
    url(r'^user_view/(?P<pk>\d+)/$', views.user_view, name='user_view'),
]
