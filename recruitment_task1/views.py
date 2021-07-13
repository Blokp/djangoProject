from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from util.util import hashPersonList


@csrf_exempt
def post(request, format='json'):

    if request.method == 'POST':
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pyData = JSONParser().parse(stream)['data_list']
        pyData = sorted(pyData, key=lambda k: (k['second_name'], k['first_name']))
        hashPersonList(pyData)
        res = {'result': pyData}
        json_data = JSONRenderer().render(res)

        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponseForbidden()
# Create your views here.
