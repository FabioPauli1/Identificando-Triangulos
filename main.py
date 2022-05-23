cateto1 = int(input('Cateto A: '))
cateto2 = int(input('Cateto B: '))
hipotenusa = int(input('Hipotenusa: '))

if cateto1+cateto2<hipotenusa or cateto1+hipotenusa<cateto2 or cateto2+hipotenusa<cateto1:
  tri = False
  print('Triangulo Inexistente')
else: 
  tri = True
  print('Triangulo existente')

  
if cateto1 == cateto2 == hipotenusa and tri == True:
  print('Triangulo Equilatero')

if cateto1 == cateto2 != hipotenusa or hipotenusa == cateto1 != cateto2 or hipotenusa == cateto2 != cateto1 and tri == True:
  print('Triangulo Isósceles')

if cateto1 != cateto2 != hipotenusa and tri == True:
  print('Triangulo Escaleno')