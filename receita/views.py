from django.shortcuts import render, get_object_or_404
from .models import Receita
from django.db.models import Q # Importamos o Q para buscas complexas

def index(request):
    receitas = Receita.objects.filter(publicado=True)
    search_term = request.GET.get('q')

    if search_term:
        # Filtra por título OU ingredientes que contenham o termo (icontains = case-insensitive)
        receitas = receitas.filter(
            Q(titulo__icontains=search_term) | 
            Q(ingredientes__icontains=search_term)
        )

    return render(request, 'index.html', {
        'receitas': receitas,
        'search': search_term
    })

def detalhe_receita(request, slug):
    receita = get_object_or_404(Receita, slug=slug)
    return render(request, 'detalhes.html', {'receita': receita})
