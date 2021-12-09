from django.shortcuts import render
#from django import HttpResponse
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import ConditionsSerializer
from .models import Conditions


def index(request):
    # temp = Conditions.objects.all().last()
    

    temp_list = Conditions.objects.all()
    ottawa = []
    whitby = []
    surrey = []
    saskatoon = []
    banff = []


    for o in temp_list:
        if o.location == "ottawa":
            ottawa.append(o)
        if o.location=="whitby":
            whitby.append(o)
        if o.location == "surrey":
            surrey.append(o)
        if o.location == "saskatoon":
            saskatoon.append(o)
        if o.location == "banff":
            banff.append(o)

    # temp_list=temp_list[::-1]
    # #temp_list = temp_list[0:5]
   #'temperature': temp, 'tempList': temp_list,

    context = {'banffList': banff, 'ottawaList': ottawa, 'whitbyList': whitby, 'surreyList': surrey, 'saskatoonList': saskatoon }

    return render(request, "index.html", context=context)



class ConditionView(viewsets.ModelViewSet):
    serializer_class = ConditionsSerializer
    queryset = Conditions.objects.all()
