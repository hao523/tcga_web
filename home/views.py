from django.shortcuts import render, render_to_response
import json as simplejson
import numpy as np
import codecs, json
from django.http import HttpResponse,JsonResponse
from django.template import RequestContext

# Create your views here.
def process_url_from_client(request):


    a = np.random.rand(20,20)
    a= a.tolist()
    file_path = "path.json"  ## your path variable
    json.dump(a, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True,
              indent=4)  ### this saves the array in .json format



    return render('home.html',RequestContext(request, {}))

def the_new_one(request):
    a = request.POST['id']
    print(a)

    return render(request, 'new_page.html', {'id':a})