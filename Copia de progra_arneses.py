import math
#acumuladores
Medida_2cables=0
Medida_3cables=0
Medida_4cables=0
Metros_azules= 0
Metros_rojos= 0
Metros_negros= 0
Metros_naranjas= 0
Metros_verdes= 0
Metros_amarillos= 0
Residuo_cable= 0


Pedidos= int(input("¿Cuantos pedidos vas a realizar?"))
contador=1
while contador <= Pedidos:
    print(f'pedido numero {contador}')
    Arnes_2cables= int(input("¿cuantos arnes de 2 cables necesitas?"))
    Arnes_3cables= int(input("¿Cuantos arnes de 3 cables necesitas?"))
    Arnes_4cables= int(input("¿Cuantos arnes de 4 cables necesitas?"))
    if Arnes_2cables>0:
          Medida_2cable+=float(input("que medida ocupas en tu arnes de 2 cables [Rango de 1.5 a 3 metros"))
    if Arnes_3cables>0:
         Medida_3cables+=float(input("¿Que medida ocupas en tu arnes de 3 cables [Rango de 1.5 a 3 metros"))
    if Arnes_4cables>0:
         Medida_4cables+=float(input("¿Que medida ocupas en tu arnes de 4 cables [30 a 80 cm]"))
    contador +=1


total_arnes=Arnes_4cables+Arnes_3cables+Arnes_2cables
if total_arnes<=0:
     print("No se coloco ningun arnes")
else:
     Metros_arnes_2_requeridos= (Arnes_2cables * Medida_2cables) + (Arnes_2cables *0.08)
     Metros_azules+=Metros_arnes_2_requeridos
     Metros_rojos+=Metros_arnes_2_requeridos


     Metro_arnes_3_requeridos= (Arnes_3cables *Medida_3cables) + (Arnes_3cables * 0.12)
     Metros_azules+= Metro_arnes_3_requeridos
     Metros_rojos+= Metro_arnes_3_requeridos
     Metros_naranjas+= Metro_arnes_3_requeridos


     metro_arnes_4_convertido=Medida_4cables/100
     Metro_arnes_4_requeridos=(Arnes_4cables*metro_arnes_4_convertido) + (Arnes_4cables * 0.16)
     Metros_negros+=Metro_arnes_4_requeridos
     Metros_azules+=Metro_arnes_4_requeridos
     Metros_verdes+= Metro_arnes_4_requeridos
     Metros_amarillos+= Metro_arnes_4_requeridos

     Residuo_cable= (Arnes_2cables *0.08) + (Arnes_3cables * 0.12) + (Arnes_4cables * 0.16)
     
     #bobinas de 1000 metros
     Cantidad_bobina_azul= math.ceil(Metros_azules/1000)
     Cantidad_bobina_negra= math.ceil(Metros_negros/1000)
     Cantidad_bobina_naranja=math.ceil(Metros_naranjas/1000)
     
     #bobinas de 500 metros 
     Cantidad_Bobina_verdes=math.ceil(Metros_verdes/500)
     Cantidad_Bobina_amarillas=math.ceil(Metros_amarillos/500)
     Cantidad_Bobina_roja=math.ceil(Metros_rojos/500)
     
     Dolar_cambio=float(input("¿Cual es el tipo de cambio de dolar el dia de hoy?"))