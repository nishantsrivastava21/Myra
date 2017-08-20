from django.contrib import admin
from alerts.models import AlertAssignee, AlertManager, Alerts

admin.site.register(AlertAssignee)
admin.site.register(AlertManager)
admin.site.register(Alerts)