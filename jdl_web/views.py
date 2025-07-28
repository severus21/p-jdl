import os
import unidecode

from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from jdl.settings import BASE_DIR
from .models import *
from .forms import *

# Create your views here.

def contact(request):
    return render(
        request,
        "projects/contact.html", {
            'title':_('JDL')
        }
    )
def informations(request):
    return render(
        request,
        "projects/informations.html", {
            'title':_('JDL')
        }
    )
def thanks(request):
    return render(
        request,
        "projects/thanks.html", {
            'title':_('JDL')
        }
    )
def method(request):
    return render(
        request,
        "projects/method.html", {
            'title':_('JDL')
        }
    )

def map(request):
    return render(
        request,
        "projects/map.html", {
            'title':_('JDL')
        }
    )

def index(request):
    ##FIXME Added here since we load each time the CSV file ...
    from .jdl_core.jdl import jdl2, homonyme
    jdl_res = {}
    alert_type, msg = '', ''


    if request.method == 'POST':
        form = GenerationForm(request.POST)

        if form.is_valid():
            city_name = unidecode.unidecode(form.cleaned_data['city_name'].strip()).upper()
            #city_name = form.cleaned_data['city_name'].upper()
            dept_code = form.cleaned_data['dept_code']

            jdl_res = jdl2(city_name, str(dept_code)) 

            if jdl_res and 'err' in jdl_res:
                #keep same form
                msg = jdl_res['err']
                alert_type = "warning"
                jdl_res = {}
        #else:
        #    form = GenerationForm()
    else:
        form = GenerationForm()

    return render(
        request,
        "projects/index.html", {
            'generation_form': form,
            'jdl_res': jdl_res, 
            'msg': msg,
            'alert_type': alert_type,
            'title':_('JDL')
        }
    )
