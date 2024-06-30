from datetime import date, timedelta
from django import forms
from .models import appointment_booking


class AppointmentForm(forms.ModelForm):
    """
    Class for users to book appointemnts
    """
    class Meta:
        """
        Model and fields
        """

        model = appointment_booking
        exclude = ['user', 'complete', ]
        presentday = date.today()
        tomorrow = presentday + timedelta(1)
        widgets = {
            'date': forms.DateInput(
                attrs={
                        'type': 'date',
                        'class': 'form-control',
                        'min': tomorrow,

                        }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please tell us about any additonal'
                    ' requirements you may have. Please let us know if you'
                    ' need any assistance with acceess.'
                    ' If you would prefer to discuss your additional'
                    'requiremnts via phone please feel free to call us'
                    'on 01456 123 456'
                })
        }
