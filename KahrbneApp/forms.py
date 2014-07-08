__author__ = 'sameedo'

from django import forms


class PhotovoltaicForm(forms.Form):
    first_num = forms.CharField()
    second_num = forms.CharField()
    third_num = forms.CharField()