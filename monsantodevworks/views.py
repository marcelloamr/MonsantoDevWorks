from django.shortcuts import render
from .models import Contact

# Função para a página inicial
def home(request):
    return render(request, 'home.html')  # Certifique-se de que 'home.html' existe no diretório templates

# Função para a página de serviços
def services(request):
    return render(request, 'services.html')  # Certifique-se de que 'services.html' existe no diretório templates

# Função para a página sobre
def about(request):
    return render(request, 'about.html')  # Certifique-se de que 'about.html' existe no diretório templates

# Função para a página de contato
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
