from django import forms
from alerts.models import Alerts

class AlertrForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlertrForm, self).__init__(*args, **kwargs)

        self.fields['reference_id'].label = "Unique Reference Id"
        self.fields['reference_id'].widget = forms.TextInput(attrs={'placeholder': 'Reference Id', 'required': 'true'})
        self.fields['reference_id'].required = True

        self.fields['delay'].label = "Dekay in resolving the issue"
        self.fields['delay'].widget = forms.TextInput(attrs={'placeholder': 'In seconds', 'required': 'true'})
        self.fields['delay'].required = True

        self.fields['description'].label = "Issue Description"
        self.fields['description'].widget = forms.TextInput(attrs={'placeholder': 'Proper description of the issue', 'required': 'true'})
        self.fields['description'].required = True

    class Meta:
        model = Alerts
        fields = ['reference_id', 'delay', 'description']