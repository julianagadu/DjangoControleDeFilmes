from django.shortcuts import redirect, render
#from django.views.generic import ListView,CreateView
from .models import Filme,Categoria
from .forms import Filmeform


# Create your views here.
def Homeview(request):
    filmes = Filme.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'listar.html',{'filmes' : filmes, 'categorias' : categorias})
    
def historico(request):
    filmes = Filme.objects.all()
    return render(request, 'base.html',{'filmes' : filmes})   

def CreateFilme(request):
    if request.method == 'POST':
        form = Filmeform(request.POST,request.FILES)
        form.save()
        return redirect('/home/')
    else:
        form = Filmeform()
        return render(request, 'filme.html', {'form':form})

def UpdateFilme(request,id):
    filme = Filme.objects.get(pk=id)
    if request.method == 'POST':
        form = Filmeform(request.POST,request.FILES,instance=filme)
        form.save()
        return redirect('/home/')
    else:
        form = Filmeform(instance=filme)
        return render(request, 'filme.html', {'form':form, 'filme':filme})

def FilmeDetail(request,id):
    filme = Filme.objects.get(pk=id)
    return render(request, 'filmedetail.html', {'filme':filme})

def DeleteFilme(request,id):
    filme = Filme.objects.get(pk=id)
    filme.delete()
    return redirect('/home/')