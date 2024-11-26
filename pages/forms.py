from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Адрес электронной почты')
    class Meta:
        fields = ['email']


class ConfirmForm(forms.Form):
    email = forms.EmailField(label='Адрес электронной почты')
    otp = forms.CharField(max_length=6, min_length=6, label='Код')
    class Meta:
        fields = ['email', 'otp']