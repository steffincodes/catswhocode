from django.forms import ModelForm
from .models import CatRoom

class CatRoomForm(ModelForm):
    class Meta:
        model = CatRoom
        fields = '__all__'
