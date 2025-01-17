from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'disabled': True, }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'disabled': True, }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)