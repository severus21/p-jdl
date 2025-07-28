'''Forms of the stock application'''
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import Form, ModelForm
from django.core.exceptions import ValidationError

from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

def validate_dept(value):
    try: 
        tmp = int(value)
        flag = (0 < tmp and tmp != 20 and tmp < 96) or (tmp in [97, 971, 972, 973, 974, 975, 976, 977, 978, 984, 986, 987, 988, 989])
    except:
        flag = value.upper() in ["2A", "2B"]

    if not flag:
        raise ValidationError(
            f'{value}s n\'est pas un code de département valide!'
        )
class GenerationForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '' 
        self.helper.form_class = 'form-inline navbar-left'
        self.helper.form_id = 'search_ref_form'


        self.helper.add_input(Submit('submit', _('Search!')))

    city_name = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class' : 'col-xs-2',
            'placeholder': _('Ville (nom avec les tirets).'),
            'id' : 'moteur',
            'onkeyup' : "controler_saisie()",
            'onclick' : "init_saisie('1')",
            'onmouseout' : "init_saisie('2')"
        }),
        max_length=50,
        required=True,
    )
    dept_code = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class' : 'col-xs-4',
            'placeholder': _('Code département'),
            'id' : 'moteur2',
            'onclick' : "code_dep_test()",
            'onmouseout' : ""
        }),
        max_length=3, required=True,
        validators=[validate_dept],
    )