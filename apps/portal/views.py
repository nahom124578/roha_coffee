# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Services
from .forms import ServiceForm 
import requests
from bs4 import BeautifulSoup

# Create your views here.

@login_required
def portal(request):
    url = "https://icons.getbootstrap.com/"
    response = requests.get(url)
    
    icons = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        icon_elements = soup.select(".bi")

        for icon in icon_elements:
            icon_class = icon.get("class")
            if icon_class and len(icon_class) > 1:
                icons.append(icon_class[1])

    return render(request, "Portal/index.html", {"icons": icons})



def icon_selector_view(request):
    url = "https://icons.getbootstrap.com/"
    response = requests.get(url)
    
    icons = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        icon_elements = soup.select(".bi")

        for icon in icon_elements:
            icon_class = icon.get("class")
            if icon_class and len(icon_class) > 1:
                icons.append(icon_class[1])

    return render(request, "Portal/icon_selector.html", {"icons": icons})

# List View
@login_required
def service_list(request):
    services = Services.objects.all()
    return render(request, 'Portal/Services/service_list.html', {'services': services})

# Detail View
@login_required
def service_detail_update(request, pk):
    service = get_object_or_404(Services, pk=pk)
    
    if request.method == 'POST':
        if "delete" in request.POST:
            service.delete()
            messages.success(request, "Service deleted successfully.")
            return redirect('service_list')
    
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully.")
            return redirect(reverse('service_update', args=[pk]))
    else:
        form = ServiceForm(instance=service)
    
    context = {
        'service': service,
        'form': form,
    }
    return render(request, 'Portal/Services/service_detail.html', context)

# Create View
@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service created successfully.")
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'Portal/Services/service_create.html', {'form': form})

# Update View
# def service_update(request, pk):
#     service = get_object_or_404(Services, pk=pk)
#     if request.method == 'POST':
#         form = ServiceForm(request.POST, request.FILES, instance=service)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Service updated successfully.")
#             return redirect('service_list')
#     else:
#         form = ServiceForm(instance=service)
#     return render(request, 'Portal/Services/service_create.html', {'form': form})

# Delete View
@login_required
def service_delete(request, pk):
    service = get_object_or_404(Services, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully.")
        return redirect('service_list')
    return render(request, 'Portal/Services/service_delete.html', {'service': service})

