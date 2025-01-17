from django.shortcuts import redirect, render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from.models import Posts, Comment

def loginPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se iniciò sesiòn correctamente')
                return redirect('/mision')
            
        messages.error(request, 'Datos incorrectos')
        
    return render(request, 'login.html')

def logoutPage(request):          
    logout(request)
    return redirect('/')
    return render(request, 'login.html')

def perfilPage(request):
    if (request.method == 'POST'):
        username= request.POST.get('username')
        email= request.POST.get('email')
        name= request.POST.get('name')
        last_name= request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'las contraseñas no coinciden')
            return redirect('/perfil')
        User.objects.create_user(username, email=email, first_name=name, last_name=last_name, password=password)
        return redirect('/login')
    return render(request, 'perfil.html')

def home_view(request):
    return render(request, 'inicio.html')# {'inicio': mision})

def mision_view(request, id = None):
    if request.method == 'POST':
        if id: 
            try:
                post = Posts.objects.get(id=id)
                if(post.user == request.user):
                    post.title = request.POST.get('title')
                    post.text = request.POST.get('text')
                    post.save()
            except Posts.DoesNotExist:
                pass
        else:
            Posts.objects.create(
                title=request.POST.get('title'),
                text=request.POST.get('text'),
                user = request.user
            )
            messages.success(request, 'Evento creado Correctamente')
                

        return redirect('/post')   
              
    context = {}   
    if id is not None:
        try:
            p =  Posts.objects.get(id=id)
            context['mision'] = p
        except Posts.DoesNotExist:
             context['mision'] = None
    
    return render(request, 'mision.html', context)

def comment(request):
    p =  Posts.objects.get(id= request.POST.get('post'))
    Comment.objects.create(
            text=request.POST.get('text'),
            user = request.user,
            post = p
    )
    return redirect('/')

def registro(request):
    return render(request, '<p>Mision de UruVene </p>')


def post(request):
   mision = Posts.objects.order_by('-created')
   return render(request, 'ejemplo.html', {'ejemplo': mision})
        

