from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('alerts.urls', namespace='alerts')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'dashboard/', include('dashboard.urls', namespace='dashboard')),
]
