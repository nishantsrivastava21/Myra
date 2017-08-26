from rest_framework_nested import routers
from alerts.views import AlertsViewSet
from django.conf.urls import patterns, include, url

router = routers.SimpleRouter()
router.register(r'alerts', AlertsViewSet, base_name="alerts")



urlpatterns = patterns('',
    url(r'^', include(router.urls)),)