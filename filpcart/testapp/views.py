from django.shortcuts import render
from . import forms

# Create your views here.
def homeview(request):
    return render(request,'testapp/home.html')

def addview(request):
    form=forms.ShopCart()
    response=render(request,'testapp/add.html',{'form':form})
    if request.method == 'POST':
        form=forms.ShopCart(request.POST)
        if form.is_valid():
            itemname=form.cleaned_data['itemname']
            price=form.cleaned_data['price']
            response.set_cookie(itemname,price,400000)
    return response

def displayview(request):
    return render(request,'testapp/display.html')
