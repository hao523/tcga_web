from django.shortcuts import render

# Create your views here.
def correlation(request):
    return render(request, 'correlation.html')


def biological(request):
    return render(request, 'biological.html')

def select(request):
    if request.method == 'POST':
        cancer_type = request.POST['cancer_type']
        feature = request.POST['feature']
        gene = request.POST['gene']
        src = feature + '.jpg'
        context={'cancer_type':cancer_type,
                 'feature':feature,
                 'src':'../../media/mrna/select'+src,
                 'gene':gene}



    return render(request, 'select.html', context)


def bio_select(request):
    if request.method == 'POST':
        cancer_type = request.POST['cancer_type']
        feature = request.POST['feature']
        threshold = request.POST['threshold']
        src = feature + '.jpg'
        context={'cancer_type':cancer_type,
                 'feature':feature,
                 'src':'../../media/mrna/bio_select/'+src,
                 'threshold':threshold,
                 }



    return render(request, 'bio_select.html', context)