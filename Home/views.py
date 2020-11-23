from django.shortcuts import render,redirect
from rifas.models import rifa
from rifas.models import skin
from rifas.models import avaliacao
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        textao = request.POST['textao']
        votacao = request.POST['votacao']
        if nome == "":
            nome="babaca não escreveu"
        if textao == "":
            textao="babaca não escreveu"
        p = avaliacao.objects.create(nota=votacao,nome=nome,texto=textao)     
        p.save()
        messages.success(request, 'Avaliação enviada')
    rifas = rifa.objects.filter(ativa="True").order_by("-num_part")[:4]
    
    dados={
        'rifa' : rifas,
        
    }
    print(rifas)
    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return render(request,'index.html', dados)

def dashboard(request):
    
    if request.method == 'POST':
        nome = request.POST['nome']
        textao = request.POST['textao']
        votacao = request.POST['votacao']
        if nome == "":
            nome="babaca não escreveu"
        if textao == "":
            textao="babaca não escreveu"
        p = avaliacao.objects.create(nota=votacao,nome=nome,texto=textao)     
        p.save()
        messages.success(request, 'Avaliação enviada')
    rifas = rifa.objects.filter(ativa="True").order_by("-num_part")[:4]
    
    dados={
        'rifa' : rifas,
        
    }
    print(rifas)
    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return render(request,'index.html', dados)