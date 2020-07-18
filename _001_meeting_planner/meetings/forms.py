from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput

from meetings.models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start': TimeInput(attrs={'type': 'time'}),
            'duration': TextInput(attrs={
                'type': 'number',
                'min': '15',
                'max': '240'
            }),
        }

    def clean_date(self):
        meeting_date = self.cleaned_data.get('date')
        if meeting_date < date.today():
            raise ValidationError('Meetings cannot be in the past!')
        return meeting_date
