import json
import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import default_storage
from .util import getDictData
from django.http import JsonResponse
from .models import ExpiryDate,Strike
from datetime import datetime

# Create your views here.
def index(request):
    context = {}

    dates = []  
    strikes = []
    for date in ExpiryDate.objects.all():
        dates.append(date.date)

    # for instrument in Instrument.objects.all():
    #     instruments.append(instrument.instrument)

    # for strike in Strike.objects.all():
    #     strikes.append(strike.strike)


    context['dates'] = dates
    # context['strikes'] = strikes
    
    return render(request,'frontend/index.html',context)

def getData(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    if 'expiryDate' not in data or 'formatedString' not in data:
        return JsonResponse({"error": "expiryDate, formatedString Required"}, status=400)    

    # print(data["expiryDate"]+ " "+ data["formatedString"])
    # return JsonResponse(data)

    
    # responseData = getDictData("13aprilexpiry", "BANKNIFTYWK37600CE")
    responseData = getDictData(data["expiryDate"], data["formatedString"])
    return JsonResponse(responseData,safe=False)

def getStrikes(request,date): 
    date = datetime.strptime(date, '%d-%B-%Y')
    
    date = date.strftime("%Y-%m-%d")
    date = ExpiryDate.objects.filter(date=date)

    strikes = list(Strike.objects.filter(date__in=date).values("strike"))
    strikes = [d['strike'] for d in strikes]
    return JsonResponse(strikes, safe=False) 
