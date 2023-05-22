from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
from django.views.generic import FormView

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('Form is saved successfully')


