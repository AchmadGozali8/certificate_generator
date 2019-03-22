from django.forms import ModelForm
from models import CertificateTemplate

class CertificateForm(ModelForm):
    class Meta:
        model = CertificateTemplate
        exclude = ["created_date", "modified_date"]