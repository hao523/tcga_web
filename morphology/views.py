from django.shortcuts import render, render_to_response

# Create your views here.
def feature_extraction(request):
    return render(request, 'feature_extraction.html')


def feature_distribution(request):
    return render(request, 'feature_distribution.html')


def search(request):
    if request.method == 'POST':
        text = request.POST['search_text']

    return render_to_response('ajax_search.html', {'text': text})

