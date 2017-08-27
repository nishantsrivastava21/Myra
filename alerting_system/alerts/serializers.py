from rest_framework import serializers

class AlertSerializer(serializers.Serializer):
    reference_id = serializers.CharField()
    delay = serializers.IntegerField()
    description = serializers.CharField()