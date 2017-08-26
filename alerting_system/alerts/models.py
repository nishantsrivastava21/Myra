from django.db import models

class AlertAssignee(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, null=False, blank=False)

class AlertManager(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)


class Alerts(models.Model):
    reference_id=models.CharField(max_length=100, null=False, blank=False, unique=True)
    delay = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    active = models.BooleanField(null=False, blank=False, default=True)
    assignee = models.ForeignKey(AlertAssignee, related_name='assignee', related_query_name='assignee')
    manager = models.ForeignKey(AlertManager, related_name='manager', related_query_name='manager')
