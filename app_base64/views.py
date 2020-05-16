from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
import json
import base64

# Create your views here.
def app_base64(request):
    get_url = str(request.get_full_path)
    print("base64 url name is {}".format(get_url))    
    if request.is_ajax():
        if 'ajax_base64.html' in str(get_url):
            return render(request, 'base64.html', {'var_page_to_load':'ajax'})
        else:
            print(request.POST)
            input_type = str(request.POST['input_type'])
            input_value = str(request.POST['input_value'])
            data = {}
            if str(input_type) in "base64encode":
                base64_encoded = base64.b64encode(bytes(input_value, 'utf-8'))  
                data['final'] = str(base64_encoded, "utf-8")
            elif  input_type in "base64decode":
                print(input_value)
                input_value += "=" * ((4 - len(input_value) % 4) % 4)
                print(input_value)
                base64_decoded = base64.b64decode(input_value)
                data['final'] = str(base64_decoded, "utf-8")

            result = json.dumps(data)
            result = json.loads(result)
            return JsonResponse(result, safe=False)
    else:
        return render(request, 'base.html', {'var_page_to_load':'base64'})
                


