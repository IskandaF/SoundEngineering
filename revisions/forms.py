from django import forms
from .models import Revision
from django.forms import ModelForm
from django.forms.widgets import NumberInput,RadioSelect
from django.forms import formset_factory


class GeneralForm(forms.ModelForm):
    class Meta:
        model=Revision
        fields='__all__' 
        widgets={
            # "track":forms.RadioSelect(),
            "track":forms.HiddenInput(),
            "project":forms.HiddenInput(),
            "volumechange":NumberInput(attrs={"type":"range",'min':'-100', 'max':'100'}),
            "panningposition":NumberInput(attrs={"type":"range",'min':'-100', 'max':'100'}),
        }
    __name__="GenForm"
    # def __init__(self, *args, **kwargs):
    #     super(GeneralForm, self).__init__(*args, **kwargs)



# class IdRevisionForm(forms.ModelForm):
#     class Meta:
#         model=Revision

#         fields=["track"]
#         widgets={
#             "track":forms.HiddenInput(),
#             "project":forms.HiddenInput(),
#         }

# class EqRevisionForm(forms.ModelForm):
#     class Meta:
#         model=Revision

#         fields=["eq_high","eq_middle","eq_low"]


# class EffectsRevisionForm(forms.ModelForm):
#     class Meta:
#         model=Revision

#         fields=["distortion_changes","reverb_changes","delay_changes"]

# class MainRevisionForm(forms.ModelForm):
#     class Meta:
#         model=Revision
#         fields=["volumechange","panningposition"]
#         widgets={
#             "volumechange":NumberInput(attrs={"type":"range",'min':'0', 'max':'100'}),
#             "panningposition":NumberInput(attrs={"type":"range",'min':'0', 'max':'100'}),
#             "track":forms.HiddenInput(),
#             "project":forms.HiddenInput(),
#         }


