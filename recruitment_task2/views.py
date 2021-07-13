from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from util.util import getJSONFromURL, calcBTCPrice


@csrf_exempt
def post(request, format='json'):

    if request.method == 'POST':

        jsonData = request.body
        stream = io.BytesIO(jsonData)
        amount = JSONParser().parse(stream)['buy']
        print(amount)
        orderbook = getJSONFromURL('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
        print(orderbook['asks'])
        res = {'price': calcBTCPrice(amount, orderbook['asks'])}
        json_data = JSONRenderer().render(res)

        return HttpResponse(json_data, content_type='application/json')
    else:
        res = {'msg': 'XDD22'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
# Create your views here.
