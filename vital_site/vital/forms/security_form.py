from django.forms import ModelForm
from django import forms
from ..models import VLAB_User
from captcha.fields import CaptchaField

class Registration_form(ModelForm):

    cleaned_data = {}
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

    class Meta:
        model = VLAB_User
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password', 'admitted_on', 'department',
                  'phone', 'captcha']

    def clean(self):
        cleaned_data = super(Registration_form, self).clean()
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data
