from django import forms 
from .models import Sales,SalesItem


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ("customer_name",)

class SalesItemForm(forms.ModelForm):
    class Meta:
        model = SalesItem
        fields = ("product","qty",)