from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class NwForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control my-2", "placeholder": "Password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control my-2", "placeholder": "Password Again"}
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "mble",
            "gdr",
            "role_type",
            "eid",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Username",
                }
            ),
            "mble": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Mobile number: ",
                }
            ),
            "eid": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Unique Id",
                }
            ),
            "role_type": forms.Select(
                attrs={
                    "class": "form-control my-2",
                }
            ),
            "gdr": forms.Select(
                attrs={
                    "class": "form-control my-2",
                }
            ),
        }
