from django import forms
from testing_app.models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"
