from django import forms
from core.models import User

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'department', 'shift_start', 'shift_end']
        widgets = {
            'shift_start': forms.TimeInput(attrs={'type': 'time'}),
            'shift_end': forms.TimeInput(attrs={'type': 'time'}),
        }