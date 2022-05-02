from django.forms import ModelForm
from .models import MediaRequest


class MediaRequestForm(ModelForm):
    class Meta:
        model = MediaRequest
        fields = '__all__'
