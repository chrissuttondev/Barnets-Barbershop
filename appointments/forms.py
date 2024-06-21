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
        exclude = ['user', 'complete']
        presentday = date.today()
        tomorrow = presentday + timedelta(1)
        print(tomorrow)
        widgets = {
            'date': forms.DateInput(
                attrs={
                        'type': 'date',
                        'min': tomorrow,
                        'class': 'form-control'
                        }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please tell us about any additonal'
                    'requirements you may have. Please let us know if you'
                    'needed any assistance with acceess.'
                })
        }



