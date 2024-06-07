from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(attrs={"placeholder": "**************"}),
            "confirm_password": forms.PasswordInput(attrs={"placeholder": "*************"}),
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.TextInput(attrs={"placeholder": "afri@gmail.com"})
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data

