from django import forms
from .models import event_registration
class registrationForm(forms.ModelForm):
    class Meta:
        model=event_registration
        exclude=['events','user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })