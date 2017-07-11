from django import forms
from django.comtrib.auth import (authenticate,
                                login,
                                logout,
                                )

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError("Incorrect Username or Password")
            if not user.is_active():
                raise forms.ValidationError("Inactive User")    
        return super(UserLoginForm, self).clean(*args, **kwargs)
