from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Clothes

# Create your views here.
def index(request):
    cloth = Clothes.objects.all()
    return render(request, 'index.html', {'cloth': cloth})

def cloth_detail(request, pk):
    cloth_detail = get_object_or_404(Clothes, pk=pk)
    return render(request, 'cloth_detail.html', {'cloth_detail': cloth_detail})

def policies(request):
    return render(request, 'policies.html')