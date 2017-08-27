from rest_framework_nested import routers
from alerts.views import AlertsViewSet
from django.conf.urls import patterns, include, url

router = routers.SimpleRouter()
router.register(r'alerts', AlertsViewSet, base_name="alerts")

#alert_router = routers.NestedSimpleRouter(router, r'alerts', lookup='reference')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),)
    #url(r'^', include(alert_router.urls)),)