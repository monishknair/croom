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

class UserRegForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    picture = forms.Filefield()
    name = forms.CharField()
    def clean(self, *args, kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        if None in [username,password,email]:
            raise forms.ValidationError("Null field")
        
        else:
            try:
                usr = User.objects.get(username=username)
            except:
                try:
                    usr = User.objects.get(email=email)
                except:
                    pass
                else:
                    raise forms.ValidationError("Email already registered")        
            else:
                raise forms.ValidationError("Username not available ")   
        return super(UserLoginForm, self).clean(*args, **kwargs)


# ERRORS MUST NOT PASS SILENTLY ...