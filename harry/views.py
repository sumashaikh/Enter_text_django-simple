from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def index(request):
#     print(request.GET)
#     return render(request, "index.html")
def index(request):
    return render(request, "index.html")


def analyze(request):
# Get the text
    print(request.GET)
    return render(request, "analyze.html")


