# -*- coding: utf-8 -*-
from django import forms

USER_TYPES = [('0','Я заказчик'),
              ('1','Я исполнитель')]

class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Введите email', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Желаемое имя пользователя', 'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control', 'autocomplete': 'off'}), label='Пароль')
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect(), label="Кто вы?")
    
    required_css_class = 'form-group'

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя пользователя', 'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}), label='Пароль')
    
    required_css_class = 'form-group'

class PostTaskForm(forms.Form):
	title = forms.CharField(max_length=140, help_text='Максимум 140 символов', widget=forms.TextInput(attrs={'placeholder': 'Введите название заказа', 'class': 'form-control'}), label='Название заказа')
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Опишите Ваш заказ', 'class': 'form-control'}), label='Описание заказа')
	cost = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Оцените заказ', 'class': 'form-control', 'min': '1'}), label='')

	required_css_class = 'form-group'

class TakeTaskForm(forms.Form):
	pass

class ChangeCommissionForm(forms.Form):
	commission = forms.FloatField(widget=forms.NumberInput, label='Введите новую комиссию в процентах (от 0 до 100)', min_value = 0.0, max_value=100.0)