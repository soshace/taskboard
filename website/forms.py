# -*- coding: utf-8 -*-
from django import forms

USER_TYPES = [('0','Я заказчик'),
              ('1','Я исполнитель')]

class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Введите email', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Желаемое имя пользователя', 'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control', 'autocomplete': 'off'}), label='Пароль')
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect(), label="Кто вы?")
    
    required_css_class = 'form-group'

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя пользователя', 'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}), label='Пароль')
    
    required_css_class = 'form-group'