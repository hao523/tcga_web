from django.shortcuts import render

# Create your views here.
def somatic(request):
    return render(request, 'somatic.html')


def select(request):
    if request.method == 'POST':
        cancer_type = request.POST['cancer_type']
        feature = request.POST['feature']
        gene = request.POST['gene']
        src = feature + '.jpg'
        context={'cancer_type':cancer_type,
                 'feature':feature,
                 'src':'../../media/somatic/'+src,
                 'gene':gene}



    return render(request, 'select.html', context)