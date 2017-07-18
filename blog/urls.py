
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.prologue, name="prologue"),
    url(r'^list/$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    url(r'^notice/$', views.notice_list, name="notice_list"),
    url(r'^notice/(?P<pk>\d+)/$', views.notice_view, name="notice_view"),

    url(r'^comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^comments/$', views.comment_list, name='comment_list'),
]
