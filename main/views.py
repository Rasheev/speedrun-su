from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Sped Ran',
        'class': 'PBP S',
        'product': products,
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_product.html", context)