from django.conf.urls import patterns, url
from dashboard import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'home/', views.DashboardView.as_view(), name='alerts-list'),
                       url(r'create/', views.AlertCreate.as_view(), name='alert-create'),)

urlpatterns = format_suffix_patterns(urlpatterns)