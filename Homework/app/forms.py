from django import forms
from app.models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["id_comp"]


class ComputerAddForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ["name_computer", "model_computer", "company_computer",
                  "price_computer", "characteristics_computer", "photo_computer"]