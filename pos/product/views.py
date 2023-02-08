from django.shortcuts import render,redirect
from django.contrib import messages
from sales.models import SalesItem
from sales.forms import SalesItemForm
from product.forms import ProductForm
from product.models import Product
from sales.forms import SalesForm

# Create your views here.


def ProductList(request):
    products = Product.objects.all()
    return render(request, "home.html",{"values":products})


def AddProduct(request):
    if request.method =="POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request,"Product Added Successfully")
        else:
            messages.error(request,"Error")
        return redirect(ProductList)
    product_form = ProductForm() 
    context = {'product_form':product_form}    
    return render(request,"add_product.html",context)
    

       