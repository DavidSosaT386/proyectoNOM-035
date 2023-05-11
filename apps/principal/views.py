
from typing import Counter
from .forms import EmpleadoForm
from django.shortcuts import redirect,render
from .models import Empleado,encuesta,respuesta,resultado
from django.db.models import Q
from django.db.models import Sum
from django.core.paginator import Paginator
from datetime import datetime

#import json


#Agregue esto sweet alert
from django.contrib import messages


# Create your views here.
brincazo = 0
brincazo2 = 0
brincazo3 = 0

def inicia(request):
    return render(request, "ini.html")

def index(request):
    page =request.GET.get('page')
    employed = request.GET.get('RPE')
    currentYear = datetime.now().year
    employed_instance = Empleado.objects.filter(RPE = employed).first()
    ans = resultado.objects.filter(empleado = employed, contestado__year = currentYear).first()
    return render(request, "layout.html",{ 'empleados': employed_instance, 'page':page, 'answer': ans} )               


def next(request, RPE, page):

    quest = encuesta.objects.all().order_by('id')
    employed = Empleado.objects.filter(RPE = RPE).first()
    paginator =  Paginator(quest, 1)
    posts= paginator.get_page(page)    
    return render(request,"siguiente.html",{'empleados':employed, 'preguntas':posts})

def back(request,RPE,page): 

    global brincazo,brincazo2,brincazo3
    if brincazo == 1 and page == '20':
        page = '6'
#yo le movi aca---jajaj soy el consta

    if brincazo2 == 2 and page == '89':
        page = '85'

    if brincazo3 == 3 and page == '94':
        page = '90'
        
    pregu = encuesta.objects.get(id=page)
    employed = Empleado.objects.filter(RPE = RPE).first()
    res = respuesta.objects.get( empleado=employed, pregunta= pregu)
    res.delete() 

    
    return redirect(next,RPE,page)

def elec(request,id,RPE,page):

    global brincazo,brincazo2,brincazo3
    ide = encuesta.objects.get(id = id) 
    employed_instance= Empleado.objects.get(RPE = RPE)
    eleccion = request.POST['eleccion']
    guard = respuesta(pregunta=ide, empleado = employed_instance, eleccion = eleccion)
    guard.save()

    




    if page == '7':

        for i in range(6):

            i=i+1
            brinco = respuesta.objects.filter(pregunta__id=i, empleado__RPE=RPE).values('eleccion').first()
            brinquito = brinco.get('eleccion')

            
            if brinquito == 1:
                page = '21'
                brincazo = 1

                

            else:
                page = '7'
                brincazo = 0
                break


    if page == '86':

        

        brinco = respuesta.objects.filter(pregunta__id=85, empleado__RPE=RPE).values('eleccion').first()
        brinquito = brinco.get('eleccion')
        
        if brinquito == 1:

            page = '90'
            brincazo2 = 2

        else:

            page = '86'
            brincazo2 = 0



    if page == '91':

        

        brinco = respuesta.objects.filter(pregunta__id=90, empleado__RPE=RPE).values('eleccion').first()
        brinquito = brinco.get('eleccion')
        
        if brinquito == 1:

            page = '95'
            brincazo3 = 3

        else:

            page = '91'
            brincazo3 = 0

    
    return redirect(next,RPE,page)


def obtenermalito(lista,i,x,empleadot,posicion):

    j=0 
    sumador2 = 0
    sumador3 = 0
    lista = []

    boleano = False   
    
    for j in range(x):
        
        malito = respuesta.objects.filter(pregunta__id = i, empleado = empleadot ).values('eleccion').first()
        i=i+1
        malitoband = malito.get('eleccion')
        lista.insert (j,malitoband)
        j=j+1

    if posicion == 1:

         for z in lista:

            if z == 0:
                boleano = True
                break

            else:
                boleano = False
        
    if posicion == 2:

        for z2 in lista:

            if z2 == 0:
                sumador2 = 1 + sumador2

        if sumador2 >= 3:
            boleano = True
            
        else:
            boleano = False


    if posicion == 3:

        for z3 in lista:

            if z3 == 0:
                sumador3 = 1 + sumador3

        if sumador3 >= 2:
            boleano = True
            
        else:
            boleano = False
            

   



    lista = []
    return boleano



def final(request, RPE):
    employed = Empleado.objects.filter(RPE = RPE).first()
    preguntas= encuesta.objects.filter(Q(categoria= 2) | Q(categoria= 3))
    comment = request.POST['comentario']

    mal = []
    respondiodo= obtenermalito(mal,1,6,employed,1)
    if respondiodo == True:
        respondiodo = obtenermalito(mal,7,2,employed,1)
        if respondiodo == False:
            respondiodo = obtenermalito(mal,9,7,employed,2)
            if respondiodo == False:
                respondiodo = obtenermalito(mal,16,5,employed,3)

    
    

    categoria1=encuesta.objects.filter(cate=1) 
    categoria2=encuesta.objects.filter(cate=2)
    categoria3=encuesta.objects.filter(cate=3)
    categoria4=encuesta.objects.filter(cate=4)
    categoria5=encuesta.objects.filter(cate=5)
    
    dominio1=encuesta.objects.filter(dominio=1)
    dominio2=encuesta.objects.filter(dominio=2)
    dominio3=encuesta.objects.filter(dominio=3)
    dominio4=encuesta.objects.filter(dominio=4)
    dominio5=encuesta.objects.filter(dominio=5)
    dominio6=encuesta.objects.filter(dominio=6)
    dominio7=encuesta.objects.filter(dominio=7)
    dominio8=encuesta.objects.filter(dominio=8)
    dominio9=encuesta.objects.filter(dominio=9)
    dominio10=encuesta.objects.filter(dominio=10)

    sumacat1= respuesta.objects.filter(empleado=employed,pregunta__in=categoria1).aggregate(total_cat=Sum('eleccion'))
    sumacat2= respuesta.objects.filter(empleado=employed,pregunta__in=categoria2).aggregate(total_cat=Sum('eleccion'))
    sumacat3= respuesta.objects.filter(empleado=employed,pregunta__in=categoria3).aggregate(total_cat=Sum('eleccion'))
    sumacat4= respuesta.objects.filter(empleado=employed,pregunta__in=categoria4).aggregate(total_cat=Sum('eleccion'))
    sumacat5= respuesta.objects.filter(empleado=employed,pregunta__in=categoria5).aggregate(total_cat=Sum('eleccion'))

    sumadom1= respuesta.objects.filter(empleado=employed,pregunta__in=dominio1).aggregate(total_dom=Sum('eleccion'))
    sumadom2= respuesta.objects.filter(empleado=employed,pregunta__in=dominio2).aggregate(total_dom=Sum('eleccion'))
    sumadom3= respuesta.objects.filter(empleado=employed,pregunta__in=dominio3).aggregate(total_dom=Sum('eleccion'))
    sumadom4= respuesta.objects.filter(empleado=employed,pregunta__in=dominio4).aggregate(total_dom=Sum('eleccion'))
    sumadom5= respuesta.objects.filter(empleado=employed,pregunta__in=dominio5).aggregate(total_dom=Sum('eleccion'))
    sumadom6= respuesta.objects.filter(empleado=employed,pregunta__in=dominio6).aggregate(total_dom=Sum('eleccion'))
    sumadom7= respuesta.objects.filter(empleado=employed,pregunta__in=dominio7).aggregate(total_dom=Sum('eleccion'))
    sumadom8= respuesta.objects.filter(empleado=employed,pregunta__in=dominio8).aggregate(total_dom=Sum('eleccion'))
    sumadom9= respuesta.objects.filter(empleado=employed,pregunta__in=dominio9).aggregate(total_dom=Sum('eleccion'))
    sumadom10= respuesta.objects.filter(empleado=employed,pregunta__in=dominio10).aggregate(total_dom=Sum('eleccion'))
    suma1= respuesta.objects.filter(empleado=employed,pregunta__in=preguntas).aggregate(total_final=Sum('eleccion'))

    guardar = resultado(empleado = employed, atencion_clinica= respondiodo, total= suma1['total_final'], 
    cat1= sumacat1['total_cat'],cat2= sumacat2['total_cat'] , cat3= sumacat3['total_cat'], cat4= sumacat4['total_cat'],
    cat5= sumacat5['total_cat'], dom1= sumadom1['total_dom'], dom2= sumadom2['total_dom'],dom3= sumadom3['total_dom']
    ,dom4= sumadom4['total_dom'], dom5= sumadom5['total_dom'], dom6= sumadom6['total_dom'], dom7= sumadom7['total_dom'],
    dom8= sumadom8['total_dom'], dom9= sumadom9['total_dom'], dom10= sumadom10['total_dom'], comentarios= comment)
    guardar.save()
    eliminar = respuesta.objects.filter(empleado = employed)
    eliminar.delete()
    
    return redirect(results, RPE)

def asignaColor(resultdos,clau):

    col1='#9be5f7'
    col2='#6bf56e'
    col3='#ffff00'
    col4=' #ffc000'
    col5='#ff0000'
    
    
    if resultdos < clau[0] :
        color=col1

    elif resultdos < clau[1] :
        color=col2

    elif resultdos < clau[2] :
        color=col3

    elif resultdos < clau[3] :
        color=col4

    elif resultdos >= clau[3] :
        color=col5

    return color


def results(request, RPE):
    currentYear = datetime.now().year
    employed = Empleado.objects.filter(RPE = RPE).first()
    resultado_instace= resultado.objects.filter(empleado = employed, contestado__year = currentYear).first()
    Rcat = resultado.objects.filter(empleado =employed, contestado__year = currentYear).values('total','cat1','cat2','cat3','cat4','cat5','dom1','dom2','dom3','dom4','dom5','dom6','dom7','dom8','dom9','dom10').first()
    

   

    colcat={}

    

    lista = [[50,75,99,140],[5,9,11,14],[15,30,45,60],[5,7,10,13],[14,29,42,58],[10,14,18,23],[5,9,11,14],[15,21,27,37],[11,16,21,25],[1,2,4,6],[4,6,8,10],[9,12,16,20],[10,13,17,21],[7,10,13,16],[6,10,14,18],[4,6,8,10]]



    i=0

    for x,y in Rcat.items():
        
        colban=asignaColor(y,lista[i])
        colcat[x]=colban

        i=i+1
    
        
    contexto = {

    'colcat' : colcat,
    
    'resultados':resultado_instace,

    'empleados':employed
    }
    messages.success(request, "Gracias por responder")
    return render(request,"final.html",contexto)

def inicioAdmin(request):
    c= request.GET.get('centro_trabajo__exact')
     
    currentYear = datetime.now().year
    if c == None:
        employed=Empleado.objects.all().count() 
        personas_res=  resultado.objects.filter(contestado__year = currentYear).count()
        per=  resultado.objects.filter(contestado__year = currentYear).values('empleado__RPE')
        p=list(per)
        po=[]
        for elem in p:
             r =elem['empleado__RPE']
             po.append(r)
        personas_no=  Empleado.objects.exclude(RPE__in= po)
        cont=Empleado.objects.exclude(RPE__in= po).count()
    else:
        employed=Empleado.objects.filter(centro_trabajo = c ).count()
        personas_res=  resultado.objects.filter(contestado__year = currentYear , empleado__centro_trabajo=c).count() 
        per=  resultado.objects.filter(contestado__year = currentYear, empleado__centro_trabajo=c).values('empleado__RPE')
        p=list(per)
        po=[]
        for elem in p:
             r =elem['empleado__RPE']
             po.append(r)
        personas_no=  Empleado.objects.filter(centro_trabajo=c).exclude(RPE__in= po)
        cont=Empleado.objects.filter(centro_trabajo=c).exclude(RPE__in= po).count()
        
    return render(request, "adminInicio.html", {'centro': c, 'contestadas':personas_res, 'total':employed ,'noco':personas_no, 'c':cont})
def resultadoAdmin(request, centro):
    currentYear = datetime.now().year
    if centro == 'None':
        personas_res=  resultado.objects.filter(contestado__year = currentYear)
    else:
        personas_res=  resultado.objects.filter(contestado__year = currentYear , empleado__centro_trabajo=centro) 
    return render(request, "adminresultados.html",{'contestaron':personas_res})    

def empleadosAdmin(request):
    c= request.GET.get('centro_trabajo__exact')
    q= request.GET.get('q')
    if c == None or c == 'None':
        employed =  Empleado.objects.all()
        if q == None:
            employed =  Empleado.objects.all()
        else:
            employed= Empleado.objects.filter(Q(RPE__icontains= q) | Q(nombre__icontains = q) | Q(apellidos__icontains = q))
    else:
        if q == None:
            employed= Empleado.objects.filter(centro_trabajo = c)
        else:
            employed= Empleado.objects.filter(Q(RPE__icontains= q) | Q(nombre__icontains = q) | Q(apellidos__icontains = q), centro_trabajo = c)
    return render(request, "adminEmpleados.html",{'empleados':employed,'centro': c,'busqueda':q})

def crearEmpleado(request):
    if request.method == 'GET':
        form = EmpleadoForm()
        contexto={
            'form':form
        }
    else:
        form = EmpleadoForm(request.POST)
        contexto={
            'form':form
        }   
        if form.is_valid:
            form.save()
            messages.success(request, "El empleado ha sido creado con exito") 
            return redirect('empleados') 
    return render(request, 'crearEmpleado.html',contexto)


def editarEmpleado(request, RPE):
    employed= Empleado.objects.get(RPE = RPE)
    if request.method == 'GET':
        form =EmpleadoForm(instance= employed)
        contexto ={
            'form':form
        }
    else:
        form = EmpleadoForm(request.POST, instance= employed)
        contexto={
            'form':form
        }   
        if form.is_valid:
            form.save()
            messages.success(request, "El empleado %s ha sido editado con exito" % RPE)
            return redirect('empleados')     
    return render(request, 'crearEmpleado.html',contexto)

def eliminarEmpleado(request, RPE):
    employed= Empleado.objects.get(RPE = RPE)
    employed.delete()
    return redirect('empleados')