from django.shortcuts import render

def list_commande(request):
    return render(request,'commande/liste.html')

