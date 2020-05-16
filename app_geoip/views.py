from django.shortcuts import render

##for geo IP
#from django.contrib.gis.geoip2 import GeoIP2
from django.template import  RequestContext
###

# Create your views here.
def app_geoip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        print(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        '''
    print(ip)
    g = GeoIP2()
    print(g.country('vikki.in'))
    try:
        print(g.city(ip))
    except Exception as e:
        print(e)
        '''
    if request.is_ajax():
        return render(request, 'geoip.html', {'var_page_to_load':'geoipa', 'var_geoip_ip': ip})
    else:
        return render(request, 'base.html', {'var_page_to_load':'geoip', 'var_geoip_ip': ip})




