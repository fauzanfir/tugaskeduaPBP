from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

data_mywatchlist = MyWatchList.objects.all()
context = {
    'nama' : 'Fauzan Firzandy Khifzan',
    'id' : '2106702756',
    'list_watchlist' : data_mywatchlist
}
def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")