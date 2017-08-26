from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import viewsets
from rest_framework import status
from django.utils import timezone
from alerts.models import Alerts

class AlertsViewSet(viewsets.ViewSet):
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        try:
            result = []
            request_arrival_time = timezone.now()
            alerts = Alerts.objects.all()
            for alert in alerts:
                result_temp = {}
                result_temp['reference_id'] = str(alert.reference_id)
                result_temp['delay'] = str(alert.delay)
                result_temp['description'] = str(alert.description)
                result.append(result_temp)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as exception:
            return Response("INTERNAL_SERVER_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
