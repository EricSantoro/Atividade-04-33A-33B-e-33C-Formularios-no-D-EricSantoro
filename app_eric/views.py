from django.shortcuts import render
from .models import sensações, motivos
from django.shortcuts import redirect
# Create your views here.
def home(request):
  sensaçõesL = sensações.objects.all()
  motivosL = motivos.objects.all()
  return render(request,'remnant.html', context={"Sensações":sensaçõesL, "motivos":motivosL})
  
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

def delete_motivos(request,id):
  motivo = motivos.objects.get(id=id)
  if request.method == "POST":
    if "confirm" in request.POST:
      motivo.delete()

    return redirect("remnant")
  return render(request, "are_you_sure.html", context={"motivos": motivos})
  
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

def delete_sensações(request,id):
  sensação = sensações.objects.get(id=id)
  if request.method == "POST":
    if "confirm" in request.POST:
      sensação.delete()

    return redirect("remnant")
  return render(request, "are_you_sensações.html", context={"sensações": sensações})

