from django.shortcuts import render, get_object_or_404
from .models import Phone
from django.shortcuts import render

def phone_list(request):
    phones = Phone.objects.all()

    sort_param = request.GET.get('sort')
    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    return render(request, 'phones/catalog.html', context)

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, 'phones/phone_detail.html', context)