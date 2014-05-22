from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns(
    '',
    url('^$', views.index, name='index'),
    url('^quote/(?P<quote_id>\d+)/$', views.detail, name='detail'),
    url('^tag/(?P<tag_id>\d+)/$', views.tag, name='tag'),
    url('^signup/$', views.signup, name='signup'),
    url('^login/$', views.log_in, name='login'),
    url('^logout/$', views.log_out, name='logout'),
    url('^submit/$', views.Submit.as_view(), name='submit'),
    )
