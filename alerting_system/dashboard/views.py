from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView
from alerts.models import Alerts
from dashboard.forms import AlertrForm
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseBadRequest, HttpResponseServerError
from django.db import IntegrityError

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


class AlertCreate(FormView):
    template_name = "dashboard/add_alert.html"
    form_class = AlertrForm

    def get_success_url(self):
        return reverse_lazy('dashboard:alerts-list')

    def form_valid(self, form, *args, **kwargs):
        try:
            alert = form.save(commit=False)
            alert.save()
            return super(AlertCreate, self).form_valid(form)
        except IntegrityError:
            return HttpResponseBadRequest("The name of a source should be unique")
        except:
            return HttpResponseServerError("INTERNAL SERVER ERROR. Please contact your us at contact@dataglen.com")
