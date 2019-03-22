# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


from models import CertificateTemplate
from forms import CertificateForm

#PDF
from reportlab.pdfgen import canvas

#PageSize
from reportlab.lib.pagesizes import letter, A4


class CertificateTemplateView(View):
    form_class = CertificateForm
    template_name = "template.html"
    success_url = 'admin'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form':form})

class GenerateCertificate(View):
    template_name = "generate_cert.html"

    def get(self, request, *args, **kwargs):
        certificates = CertificateTemplate.objects.all()
        ctx = {
            'certificates':certificates
        }

        return render(request, self.template_name, ctx)

    
