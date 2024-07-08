nombre = input("ingrese su nombre: ")
apellido1 = input('ingrese su primer apellido:')
apellido2 = input('ingrese su segundo apellido:')
edad = int(input("ingrese su edad en años: "))
altura = float(input("ingrese su estatura en metros: "))
peso = float (input("ingrese su peso en kilogramos :"))
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = peso / altura**2
    
print("IMC: " + str(IMC) )

    #Hacemos las distintas validaciones

if IMC <= 18.49:
        print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99:
        print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad grado 1")
elif IMC >= 35.00 and IMC <= 39.99:
        print ("obesidad grado 2")
elif IMC >= 40.00:
        print ("obesidad grado 3")

#Las variables dadas en la primera parte se utilizaaron
#   como referente a la informacion que se pide agregar. 
#Input se utilozara para generar una interaccion entre
#   el programa y el usuario,permitiendo agragar la informacion solicitada.
#El comando int se utilizo para permitir ingresar un numero entero
#Por otro lado el comando float se utilizo,
#   porque en esta parte la informacion solocitada
#   sera necesario ingresar numeros con punto decimal. 
#Para obtener el calculo del IMC se tomo como referencia 
#   las variables que pide la formula del IMC comentada 
#   antes ya en la linea de comando.
# Por ultimo para mostrar el IMC se pide que haga una impresion 
# del IMC=... esto en cadena de texto, pero mas el IMC tipado en STR

#Las validaciones las tome como referencia de otros programas de ejemplo
#  y solo tuve que analizar para que servia cada uno de los elementos que 
# que se presentan ahi y con ayuda de los tutoriales cargados en el modulo 1
# lo unico que no entirndo aqui son los comandos if y elif; lo demas se ira
# fortaleciendo con la practica.  