from django.shortcuts import render,redirect
from .models import Sales, SalesItem
from .forms import SalesItemForm
from .forms import SalesForm
from django.contrib import messages
from product.views import ProductList
from sales.pdf import html_to_pdf
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def NewSales(request):
    if request.method =="POST":
        sale_form = SalesForm(request.POST)
        if sale_form.is_valid():
            sale_form.save()
            messages.success(request,"PURCHASE DONE")
        else:
            messages.error(request,"Error")
        return redirect(ProductList)
    
    items = SalesItem.objects.all()
    sale_form = SalesForm()
    sale_item_form = SalesItemForm()
    context = {"sale_form":sale_form,"sale_item_form":sale_item_form,"items":items}
    return render(request,"sales.html",context) 

def Report(request):
    sales = Sales.objects.all()
    context = {"sales":sales}
    return render(request,"report.html",context)

def PDFReport(request,id):
    print(id)
    sales = Sales.objects.get(pk=id)
    items = SalesItem.objects.filter(sales_id=sales)
    open("templates/pdf_out.html", "w").write(
        render_to_string("sales_export_pdf.html", {"sales":sales,"items":items}))
    pdf = html_to_pdf("pdf_out.html")
    return HttpResponse(pdf, content_type="application/pdf")