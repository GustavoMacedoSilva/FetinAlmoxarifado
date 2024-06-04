from django.shortcuts import render

def contato_page(request):
    return render(request, "contato.html")