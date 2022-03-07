from django import forms
class ShopCart(forms.Form):
    itemname=forms.CharField()
    price=forms.IntegerField()
