
 #Metodo para Ingresar puntuacion y comentario
def valoracion():
        while True:
                print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                point = input()
                
                if point.isdecimal():
                    point = int(point)
                    
                    if point <= 0 or point > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                        print('Indíquelo en una escala de 1 a 5')
                    else:
                        print('Por favor, introduzca un comentario')
                        comment = input()
                        post = f'punto: {point} comentario: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write(f'{ post } \n')
                        file_pc.close()
                        break
                else:
                    print('Por favor, introduzca la puntuación en números')
                    
def valoraciones_pasadas():
    #Método para comprobar los resultados anteriores
        print('Resultados hasta la fecha:')
        try:
            with open("data.txt", "r") as read_file:
                contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("No hay resultados registrados aún.")
        except FileNotFoundError:
            print("No hay resultados registrados aún.")

                    
    
def menu():
    #Menú principal 
        while True:
            print('\nSeleccione el proceso que desea aplicar')
            print('1: Ingresar puntuación y comentario')
            print('2: Comprueba los resultados obtenidos hasta ahora.')
            print('3: Finalizar')
            num = input()
        
            if num.isdecimal():
                num = int(num)
                if num == 1:
                    valoracion()
                elif num == 2:
                    valoraciones_pasadas()
                elif num == 3:
                    print('Finalizando')
                    break
                else:
                    
                    print('Introduzca un número del 1 al 3')
            else:
                print('Introduzca un número del 1 al 3')

# Ejecutar el menú principal
menu()