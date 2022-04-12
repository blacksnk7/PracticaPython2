#Esta funcion recibe los archivos, los convierte a listas y luego itera cada uno para sumar ambas evaluaciones y guardar el resultado en un diccionario donde la clave es el elemento del primer archivo y el dato es la suma del elemento en el 2do y 3er archivo.
#La funcion requiere que los 3 archivos sean de la misma longitud.
def add_grades(names, eval1, eval2):
    total = {}
    list_names = names.read().replace(",", "").split()
    list_eval1 = eval1.read().replace(",", "").split()
    list_eval2 = eval2.read().replace(",", "").split()
    for i in range(len(list_names)):
        total[list_names[i]] = int(list_eval1[i]) + int(list_eval2[i])
    return total

#Esta funcion recibe un diccionario, itera cada elemento y devuelve el promedio entre todos ellos. Se espera que la estructura recibida tendra datos de tipo int o float.
def avarege(grades):
    total = 0
    counter = 0
    for grade in grades:
        total += grades[grade]
        counter += 1
    return (total/counter)
    
#Esta funcion recibe un diccionario donde cada clave es un nombre y cada dato es un numero. Luego llama a "avarege" para calcular el promedio entre todos los datos y finalmente recorre el diccionario recibido para buscar e imprimir que datos estan por debajo del promedio de toda la estructura.   
def below_avarege(grades):
    avr = avarege(grades)
    for key in grades:
        if (grades[key] < avr):
            print(f"El alumno {key} con nota {grades[key]} esta por debajo del promedio de {avr:.2f}")
    

names = open('nombres_1.txt',  encoding='utf8')
eval1 = open('eval1.txt')
eval2 = open('eval2.txt')
total_grades = add_grades(names, eval1, eval2)
below_avarege(total_grades)
names.close()
eval1.close()
eval2.close()