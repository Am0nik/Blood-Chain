from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User
class CustomUserCreationForm(UserCreationForm):
    terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="I agree to the Terms and Conditions"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'full_name', 'blood_type', 'phone_number', 'photo', 'terms','email'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'terms':
                field.widget.attrs.update({'class': 'form-control'})


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'full_name', 
            'blood_type', 
            'phone_number', 
            'photo'
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
