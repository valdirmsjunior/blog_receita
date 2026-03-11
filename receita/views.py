from django.shortcuts import render, get_object_or_404
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.filter(publicado=True)
    return render(request, 'index.html', {'receitas': receitas})

def detalhe_receita(request, slug):
    receita = get_object_or_404(Receita, slug=slug)
    return render(request, 'detalhes.html', {'receita': receita})
