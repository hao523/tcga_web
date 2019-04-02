from django.shortcuts import render

# Create your views here.
def across(request):
    return render(request, 'across.html')


def specific(request):
    return render(request, 'specific.html')