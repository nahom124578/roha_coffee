from django.shortcuts import render
from .models import CatalogSection

def landing_page(request):
    catalog_section = CatalogSection.objects.prefetch_related('items').first()
    return render(request, 'landing_page.html', {'catalog_section': catalog_section})
