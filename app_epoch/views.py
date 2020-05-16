from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import  RequestContext
from datetime import datetime
import pytz
import json
import os
from tools.settings import BASE_DIR

# Create your views here.
def app_epoch(request):
    get_url = str(request.get_full_path)    
    if request.is_ajax():
        if 'ajax_epoch.html' in str(get_url):
            return render(request, 'epoch.html', {'var_page_to_load':'ajax'})
        else:
            epoch_to_convert = str(request.GET['epoch_to_convert'])
            if not "datetoepoch" in (epoch_to_convert):                
                epoch_to_convert = int(epoch_to_convert)
                tz_to_convert = str(request.GET['tz_to_convert'])
                tz = pytz.timezone(tz_to_convert)
                dt = datetime.fromtimestamp(epoch_to_convert, tz)
                data = {}                
                data["vara0"] = dt.strftime('%a,%b %d,%Y, %H:%M:%S %Z%z')
                r = json.dumps(data)
                data = json.loads(r)
                return JsonResponse(data, safe=False)
            elif "datetoepoch" in (epoch_to_convert):
                time_to_convert = str(request.GET['time_to_convert'])
                tz_to_convert = str(request.GET['tz_to_convert'])
                tz = pytz.timezone(tz_to_convert)
                time_format = '%a,%b %d,%Y, %I:%M:%S %p'
                datetime_object_tz = datetime.strptime(time_to_convert, time_format)
                dt_with_tz = tz.localize(datetime_object_tz, is_dst=None)
                dt_with_tz_epoch = (dt_with_tz - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()
                data = {}
                data["vara0"] = dt_with_tz_epoch
                r = json.dumps(data)
                data = json.loads(r)
                return JsonResponse(data, safe=False)
    else:
        return render(request, 'base.html', {'var_page_to_load':'epoch'})