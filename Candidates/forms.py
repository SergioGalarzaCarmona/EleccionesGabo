from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from Users.models import Candidates

class VoteForm(forms.Form):
    candidate_id = forms.IntegerField(widget=forms.HiddenInput())
    
    def save(self,user, active=False):
        if not user and isinstance(user, User):
            raise ValidationError('El usuario no existe o ya votó.')# Deactivate the user after voting
        if active:  
            user.is_active = False
            user.save()
        candidate = self.cleaned_data.get('candidate')
        if candidate:
            candidate.votes += 1
            candidate.save()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        