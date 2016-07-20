from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Libro,Categoria,Autor
from .forms import LibroForm,AutorForm,CategoriaForm
from django.contrib import messages



def libreria_home(request):
    autor=Autor.objects.all()
    query_list = Libro.objects.all()
    paginator = Paginator(query_list, 3)
    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)
    context={
        "lista":query,
        "listos":autor,
    }
    return render(request,"index.html", context)

def lista_libreria(request):
    query_list = Libro.objects.all().order_by("creado")
    paginator = Paginator(query_list, 3)
    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)
    context = {
        "lista":query,
        }
    return render(request,"libro.html", context)


def detalle_libreria(request,id=None):
    query=get_object_or_404(Libro,pk=id)
    context={
        "detalle":query
    }
    return render(request,"detalle.html",context)

def crear_libreria(request):
    form=LibroForm(request.POST  or None,request.FILES or None)
    if form.is_valid():
        libro=form.save(commit=False)
        libro.save()
        messages.success(request,'fue creado exitosamente')
        return HttpResponseRedirect('/libro/')
    context={
        "form":form,
    }
    return render(request,"form_libro.html",context)

def actualizar_libreria(request,id=None):
    query=get_object_or_404(Libro,pk=id)
    form=LibroForm(request.POST  or None,request.FILES or None,instance=query)
    if form.is_valid():
        libro=form.save(commit=False)
        libro.save()
        messages.success(request,'fue actualizado exitosamente')
        return HttpResponseRedirect('/libro/')
    context={
        "detalle":query,
        "form":form,
    }
    return render(request,"form_libro.html",context)

def borrar_libreria(request, id=id):
    query=get_object_or_404(Libro,pk=id)
    query.delete()
    messages.success(request,'fue borrada tu informacion de manera incorrecta')
    return redirect("/libro/")



def lista_categoria(request):
    query_list = Categoria.objects.all()
    paginator = Paginator(query_list, 3)
    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)
    context = {
        "lista":query,
        }
    return render(request,"categoria.html", context)

def detalle_categoria(request,id=None):
    query=get_object_or_404(Categoria,pk=id)
    context={
        "detalle":query
    }
    return render(request,"categoria_detalle.html",context)

def crear_categoria(request):
    form=CategoriaForm(request.POST  or None,request.FILES or None)
    if form.is_valid():
        categoria=form.save(commit=False)
        categoria.save()
        messages.success(request,'fue creado exitosamente')
        return HttpResponseRedirect('/categoria/')
    context={
        "form":form,
    }
    return render(request,"form_categoria.html",context)

def actualizar_categoria(request,id=None):
    query=get_object_or_404(Categoria,pk=id)
    form=CategoriaForm(request.POST  or None,request.FILES or None,instance=query)
    if form.is_valid():
        categoria=form.save(commit=False)
        categoria.save()
        messages.success(request,'fue actualizado exitosamente')
        return HttpResponseRedirect('/categoria/')
    context={
        "detalle":query,
        "form":form,
    }
    return render(request,"form_categoria.html",context)

def borrar_categoria(request, id=id):
    query=get_object_or_404(Categoria,pk=id)
    query.delete()
    messages.success(request,'fue borrada tu informacion de manera incorrecta')
    return redirect("/categoria/")










def lista_autor(request):
    query_list = Autor.objects.all().order_by("actualizado")
    paginator = Paginator(query_list, 3)
    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)
    context = {
        "lista":query,
        }
    return render(request,"autor.html", context)

def detalle_autor(request,id=None):
    query=get_object_or_404(Autor,pk=id)
    context={
        "detalle":query
    }
    return render(request,"autor_detalle.html",context)

def crear_autor(request):
    form=AutorForm(request.POST  or None,request.FILES or None)
    if form.is_valid():
        autor=form.save(commit=False)
        autor.save()
        messages.success(request,'fue creado exitosamente')
        return HttpResponseRedirect('/autor/')
    context={
        "form":form,
    }
    return render(request,"form_autor.html",context)

def actualizar_autor(request,id=None):
    query=get_object_or_404(Autor,pk=id)
    form=AutorForm(request.POST  or None,request.FILES or None,instance=query)
    if form.is_valid():
        autor=form.save(commit=False)
        autor.save()
        messages.success(request,'fue actualizado exitosamente')
        return HttpResponseRedirect('/autor/')
    context={
        "detalle":query,
        "form":form,
    }
    return render(request,"form_autor.html",context)

def borrar_autor(request, id=id):
    query=get_object_or_404(Autor,pk=id)
    query.delete()
    messages.success(request,'fue borrada tu informacion de manera incorrecta')
    return redirect("/autor/")
