from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.forms import MascotaForm,Datos_PersonalesForm
from blog.models import Mascota, Usuario
from .forms import RegistroForm


# Create your views here.
def post_list(request):
    
    return render(request, 'blog/post_list.html', {})

def post_new(request):
    if request.method == 'POST':
        form = Datos_PersonalesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('blog/post_list.html')
    else:
        form = Datos_PersonalesForm()
    return render(request, 'blog2/post_new.html')
    a = request.GET['nombre']

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('blog/post_list.html')
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form':form})   

def mascota_list(request):
    mascota = Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form':form}) 

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota}) 

def registroUsuario(request):
	### *** inicio: se incluye las variables para que sean agregados al formulario o vista html
	form = RegistroForm(request.POST or None) ## clase declarada en forms.py
	### *** fin

	print ("Este mensaje aparece en la consola donde esta ejectandose el comando runserver")
	# print(dir(form)) # funciones disponible con el form

	# captura de los datos que fueron enviados por el usuario con el metodo POST
	# se valida para no tener error de lectura de datos
	if form.is_valid():
		datos = form.cleaned_data
		print (datos.get("nombre"))
		print (datos.get("email"))

		# se guarda en la bdd
		nombre = datos.get("nombre")
		email = datos.get("email")
		
		objetoUsuario = Usuario()
		objetoUsuario.nombre = nombre
		objetoUsuario.email = email
		objetoUsuario.save()
		return render(request, "exitoRegistroUsuario.html", {"usuario":objetoUsuario})


	### *** inicio: se incluye en la linea de abajo, las variables declaradas en el archivo forms.py
	contexto = {"formulario" : form}
	## en la clase regitroUsuario
	### *** fin
	return render(request, "inicio.html", contexto)

### 
### Crear archivo forms.py en la raiz del proyecto y su contenido
### despues agregar los codigos señalado con ***
 


