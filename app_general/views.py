from django.shortcuts import render
#from django.http import  HttpResponse, JsonResponse

# Create your views here.
def app_general(request):
    get_url = str(request.get_full_path)
    print(get_url)
    return render(request, 'base.html', {'var_page_to_load':'general'})