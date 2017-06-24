'''
message = "Hola Mundo, Hey"
print message
numer = 500
if numer == 500:
   print "El numero es igual a 500"
elif numer < 500:
   print "El numero es menor a 500"
else:
   print "El numero es mayor a 500"
nombre = ['Edhuin',46,'Carlos',30,'Leonidas']
print nombre[2]
nombre.append(38)
for x in nombre:
   print x
'''

alumno = {'nombre':'Edhuin',
	  'edad':46,
	  'direccion':'Av.Oscar R.Benavides 3046'}
#print alumno['direccion']

def PrintDictionary(TheDictionary):
   for key in TheDictionary:
	print key + "=" + str(TheDictionary[key])

PrintDictionary(alumno)

var = 26
result = var > 25 and 'Mayor de 25' or 'Menor de 25'
print result

