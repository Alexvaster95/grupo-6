# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


A=int(input("ingrese un numero\n"))  
B=int(input("ingrese otro numero\n"))  
C=int(input("ingrese un nuemero\n")) 
if(A > B and A < C or A < B and A > C):  
 print("El numero intermedio es " + str(A))  
else:  
 if(B > A and B < C or B < A and B > C):  
  print("El numero intermedio es " + str(B))  
 else:  
  if(C > A and B < C or C < A and C > B ):
     print("El nuemro intermedio es " + str (C))
  else:
      print ("No esxiste el nuemro intermedio")
 