from django.shortcuts import render, HttpResponse, redirect
from  .forms import DocenteForm


# Create your views here.

html_base = """
     <h1>Tienda Virtual Liz Fashion</h1>
     <ul>
            <l1>    <a href="/">Portada</a>   </l1>
            <l1>     <a href="/docentes/">Docente</a>  </l1>
            <l1>     <a href="/contact/">Contacto</a>   </l1>
            <l1>     <a href="/portfolio/">Portafolio</a>   </l1>



     </ul>
"""

## pagina inidical del crud  SELECT
def docentes(request, template_name="docentes.html"):
    return render(request, template_name)

## pagina de crear o insertart UPDATE
def modificardocente(request, template_name="modificardocente.html"):
    return render(request, template_name)



## pagina de crear o insertart INSERT
def creardocente(request, template_name="creardocente.html"):

    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('docentes')
    else:
        form=DocenteForm

    return render(request, template_name, {'docente':form})

## pagina de borrado o eliminar docente DELETE
def eliminardocente(request, template_name="eliminardocente.html"):
    return render(request, template_name)



def home(request,plantilla="home.html"):
    return render(request,plantilla)

def contact(request,plantilla="contact.html"):
    return render(request,plantilla)

def portfolio(request,plantilla="portfolio.html"):
    return render(request,plantilla)





