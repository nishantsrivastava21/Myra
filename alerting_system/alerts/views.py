from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import viewsets
from rest_framework import status
from django.utils import timezone
from alerts.models import Alerts
from alerts.serializers import AlertSerializer

class AlertsViewSet(viewsets.ViewSet):
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'reference_id'

    def list(self, request):
        try:
            final_result = {}
            result = []
            alerts = Alerts.objects.all()
            for alert in alerts:
                result_temp = {}
                result_temp['reference_id'] = str(alert.reference_id)
                result_temp['delay'] = str(alert.delay)
                result_temp['description'] = str(alert.description)
                result.append(result_temp)
            final_result['alerts'] = result
            return Response(final_result, status=status.HTTP_200_OK)
        except Exception as exception:
            return Response("INTERNAL_SERVER_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = AlertSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    id = self.request.data['reference_id']
                    delay = self.request.data['delay']
                    description = self.request.data['description']
                    alert = Alerts.objects.create(reference_id=id,
                                                  delay=delay,
                                                  description=description)
                    alert.save()
                    return Response(data=self.request.data, status=status.HTTP_201_CREATED)
                except Exception as exception:
                    return Response("There is another alert with same reference Id. Please provide a new one", status=status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            return Response("INTERNAL_SERVER_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, reference_id=None):
        try:
            reference_id = request.GET.get("reference_id")
            try:
                alert  = Alerts.objects.get(reference_id=reference_id)
            except:
                return Response("Invalid Reference Id", status=status.HTTP_400_BAD_REQUEST)
            alert.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as exception:
            print str(exception)
            return Response("INTERNAL_SERVER_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
