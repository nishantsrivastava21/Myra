from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView
from alerts.models import Alerts

# Create your views here.

class DashboardView(TemplateView):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        alerts = Alerts.objects.all()
        user_name = self.request.user
        context['first_name'] = user_name.first_name
        context['alerts'] = alerts
        return context
