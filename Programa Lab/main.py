from personaje import Personaje
from humano import Humano
from enano import Enano
from elfo import Elfo
import random
humano=Humano("Oscar","Humano","Espada",200,30,0,"Almua","Humano")
elfo=Elfo("Alcor","Elfo","Arco",190,25,0,"Aldum","Elfo")
enano=Enano("Torni","Enano","Daga",150,19,0,"Mechanti","Enano")
humano2=Humano("Manolo","Humano","Maza",200,40,0,"Astora","Humano")
elfo2=Elfo("Metza","Elfo","Lanza",190,45,0,"Cienaga","Elfo")
enano2=Enano("Erelio","Enano","Martillo",150,30,0,"Lagyan","Enano")
humano3=Humano("Raulin","Humano","Espadon",200,60,0,"Aratros","Humano")
elfo3=Elfo("Amador","Elfo","Baston",190,35,0,"Deus","Elfo")
enano3=Enano("Grindy","Enano","Garrote",150,25,0,"Aqua","Enano")
lista_humano=['humano','humano2','humano3']
lista_elfo=['elfo','elfo2','elfo3']
lista_enano=['enano','enano2','enano3']

seleccionlista1 = random.randint(1,3)
seleccionlista2 = random.randint(1,3)
seleccionp1 = random.randint(0,2)
seleccionp2 = random.randint(0,2)

while seleccionp1 == seleccionp2:
    seleccionp2 = random.randint(0,2)
    
if seleccionlista1 ==1:
    humano = lista_humano[seleccionp1]  
if seleccionlista1==2:
    elfo = lista_elfo[seleccionp1]
if seleccionlista1==3:
    enano = lista_enano[seleccionp1]
if seleccionlista2 ==1:
    humano2 = lista_humano[seleccionp2]  
if seleccionlista2==2:
    elfo2 = lista_elfo[seleccionp2]
if seleccionlista2==3:
    enano2 = lista_enano[seleccionp2]

def combate():
    for i in range(10):
        if seleccionp1 == Elfo:
            seleccionp1.Getvida= seleccionp1.Getvida - seleccionp2.GetDaño
            seleccionp2.Getvida= seleccionp2.Getvida - seleccionp1.GetDaño
        if seleccionp1 == Humano:
            seleccionp1.Getvida= seleccionp1.Getvida - seleccionp2.GetDaño
            seleccionp2.Getvida= seleccionp2.Getvida - seleccionp1.GetDaño         
        if seleccionp1 == Enano:
            seleccionp1.Getvida= seleccionp1.Getvida - seleccionp2.GetDaño
            seleccionp2.Getvida= seleccionp2.Getvida - seleccionp1.GetDaño

combate()    
    
    
          