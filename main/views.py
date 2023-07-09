from pathlib import Path
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def other(request, name="index"):
    if Path(f"templates/{name}.html").exists():
        return render(request, name + ".html")
    return HttpResponseNotFound()
