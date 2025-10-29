from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Person, Product
from .forms import UploadProduct

def djangoapp_view(request):
    person_list = Person.objects.all()
    return render(request, 'djangoapp.html', {'persons': person_list})

def person(request, slug):
    my_person = get_object_or_404(Person, slug=slug)
    return render(request, 'person.html', {'person': my_person})

@login_required(login_url="/users/login/")
def product_list_view(request):
    if request.method == 'POST':
        form = UploadProduct(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('djangoapp:product_list')
    else:
        form = UploadProduct()
    
    product_list = Product.objects.all()[:20]
    return render(request, 'products/list.html', {
        'product_list': product_list,
        'form': form
    })