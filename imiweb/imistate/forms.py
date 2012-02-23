from django.forms import ModelForm

from imistate.models import *

class EntityForm(ModelForm):
    class Meta:
        model = Entity