hora=int(input("Digite el tiepo em horas que estuvó en el parqueadero"))
minutos=int(input("Digite el tiempo en minutos"))

if minutos>0 and minutos<60:
   totalpagar=(hora+1)*1500
   
else:
     totalpagar=hora*1500



print(f'usted duro {hora} horas y {minutos}  minutos el total a pagar es de {totalpagar} ')
print("El total del parqueadero es de ",totalpagar)
