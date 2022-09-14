from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'id': '2106702756',
        'nama': 'Fauzan Firzandy Khifzan'
    }

    return render(request, "katalog.html", context)
