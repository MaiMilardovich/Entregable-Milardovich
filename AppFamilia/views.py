from django.shortcuts import render
from AppFamilia.models import Familia


# Create your views here.

def familia (request):

    familiar1 = Familia(nombre="Hugo" , edad = 73 , fechaNacimiento = "1949-04-01" , relacion = "Padre")

    familiar1.save()
  
    familiar2 = Familia(nombre="Liliana" , edad = 64 , fechaNacimiento = "1958-05-23" , relacion = "Madre")

    familiar2.save() 

    familiar3 = Familia(nombre="Michele" , edad = 27 , fechaNacimiento = "1995-03-11" , relacion = "Novio")

    familiar3.save()

    familiar4 = Familia(nombre="Gala" , edad = 9 , fechaNacimiento = "2013-01-23" , relacion = "Perrita")

    familiar4.save()

    return render(request , "AppFamilia/familia.html")


