from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from.models import Posts, post

def home_view(request):
    mision = Posts.objects.all()
    return render(request, 'inicio.html', {'inicio': mision})

def mision_view(request, id = None):
    if request.method == 'POST':
        Posts.objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text')
        )
        id = request.POST.get('id')    
    context = {}   
    if id is not None:
        p =  Posts.objects.get(id = id)
        context['mision'] = p
    
    return render(request, 'mision.html', context)

def perfil(request):
    return render(request,'perfil.html')
def registro(request):
    return HttpResponse('<p>Mision de UruVene </p>')
def post(request):
    if request.method == 'POST':
        post.Objects.create(
            title = request.POST.get('title'),
            text = request.POST.get('text')
            
            
        )
    return render(request, 'ejemplo.html')


