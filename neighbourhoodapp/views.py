from neighbourhoodapp.models import NeighbourHood
from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def neighbourhoods(request):
    hoods = NeighbourHood.objects.all()
    return render(request, {'hoods': hoods} )

