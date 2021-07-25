from neighbourhoodapp.models import NeighbourHood
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from django.shortcuts import render
from .forms import NeighbourHoodForm, UserCreationForm, ProfileForm

# Create your views here.
def index(request):
    hoods = NeighbourHood.objects.all()
    return render(request, 'index.html', {'hoods': hoods})


def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})