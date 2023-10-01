from django.shortcuts import render
from .models import sensações, motivos
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
  sensaçõesL = sensações.objects.all()
  motivosL = motivos.objects.all()
  return render(request,'remnant.html', context={"Sensações":sensaçõesL, "motivos":motivosL})
@login_required  
def create_motivos(request):
  if request.method == 'POST':
    motivos.objects.create(
      title = request.POST['title'],
      mecanica = request.POST['mecanica'],
      concorda = request.POST['concorda'],
      ja_jogou = request.POST['ja_jogou']
   )
    return redirect('remnant') 
  return render(request,'forms.html', context={"action": "Adicionar"})
@login_required
def update_motivos(request, id):
    motivo = motivos.objects.get(id=id)
    if request.method == "POST":
        motivo.title = request.POST["title"]
        motivo.mecanica = request.POST["mecanica"]
        motivo.concorda = request.POST["concorda"]
        motivo.ja_jogou = request.POST["ja_jogou"]
        motivo.save()
        
        return redirect("remnant")
    return render(request, "forms.html", context={"action": "Atualizar", "motivos": motivos})
@login_required
def delete_motivos(request,id):
  motivo = motivos.objects.get(id=id)
  if request.method == "POST":
    if "confirm" in request.POST:
      motivo.delete()

    return redirect("remnant")
  return render(request, "are_you_sure.html", context={"motivos": motivos})
@login_required  
def create_sensações(request):
  if request.method == 'POST':
    sensações.objects.create(
      title = request.POST['title'],
      dificuldade = request.POST['dificuldade'],
      fez = request.POST['fez'],
      prazer = request.POST['prazer']
   )
    return redirect('remnant') 
  return render(request,'formssensações.html', context={"action": "Adicionar"})
@login_required
def update_sensações(request,id):
    sensação = sensações.objects.get(id=id)
    if request.method == "POST":
        sensação.title = request.POST["title"]
        sensação.dificuldade = request.POST["dificuldade"]
        sensação.fez = request.POST["fez"]
        sensação.prazer = request.POST["prazer"]
        sensação.save()
        
        return redirect("remnant")
    return render(request, "formssensações.html", context={"action": "Atualizar", "sensações": sensações})
@login_required
def delete_sensações(request,id):
  sensação = sensações.objects.get(id=id)
  if request.method == "POST":
    if "confirm" in request.POST:
      sensação.delete()

    return redirect("remnant")
  return render(request, "are_you_sensações.html", context={"sensações": sensações})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("remnant")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("remnant")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")