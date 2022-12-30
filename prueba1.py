

def verificar(entrada):
  valido=1
  if len(entrada)<=100:
    for i in range(len(entrada)):
      if(len(entrada[i])>=5000):
        valido=0
  return valido

def condicion(entrada):
  while True:  
       if '()' in entrada :  
           entrada = entrada.replace ( '()' , '' )  
       elif '{}' in entrada :  
           entrada = entrada.replace ( '{}' , '' )  
       elif '[]' in entrada :  
           entrada = entrada.replace ( '[]' , '' )
       else :  
           return not entrada

entrada=[ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]
if verificar(entrada)==1:
  for i in range(len(entrada)):
    condicion(entrada[i])
    print(f' Es válido {entrada[i]}? : {int(condicion(entrada[i]))}') 
else:
  print('No válido')