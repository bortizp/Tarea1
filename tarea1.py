from statistics import mode, StatisticsError


estudiantes = [
    {"nombre": "ana", "notas": [3.1,4.5,2.8]},
    {"nombre": "luis", "notas": [4.0,3.6,4.2]},
    {"nombre": "maria", "notas": [2.9,3.8,4.0]},
    {"nombre": "carlos", "notas": [3.5,4.1,3.9]},
    {"nombre": "sofia", "notas": [4.3,4.0,4.5]}   
]

#1. Calcula el promedio de notas de cada estudiante y determina quien tiene el promedio más alto y el más bajo
def calcular_promedio(estudiantes):
    for estudiante in estudiantes:
        estudiante["promedio"] = round(sum(estudiante["notas"])/len(estudiante["notas"]),1)
        print(f"El promedio de {estudiante['nombre']} es: {estudiante['promedio']}")

    """La clave esta en la funcion max y min,
    el cual recorre toda la lista en busca del mas alto y el mas bajo
    y devuelve el objeto completo del estudiante."""
    estudiante_mas_alto = max(estudiantes, key=lambda x: x["promedio"])
    estudiante_mas_bajo = min(estudiantes, key=lambda x: x["promedio"])

    print(f"El estudiante con el promedio más alto es: {estudiante_mas_alto['nombre']} con un promedio de: {estudiante_mas_alto['promedio']}")
    print(f"El estudiante con el promedio más bajo es: {estudiante_mas_bajo['nombre']} con un promedio de: {estudiante_mas_bajo['promedio']}")
    print(50*"*")

#2. Cuenta cuantos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0)
def aprobados(estudiantes):
    aprobados = 0
    for estudiante in estudiantes:
        if all(nota >= 4.0 for nota in estudiante["notas"]):
            aprobados += 1
    print(f"Cantidad de estudiantes aprobados: {aprobados}")
    print(50*"*")

#3. Calcula la moda de las notas de todos los estudiantes
def moda(estudiantes):
    todas_las_notas = [nota for estudiante in estudiantes for nota in estudiante["notas"]]
    try:
        # importe mode de statistics
        moda_notas = mode(todas_las_notas)
        print(f"La nota que más se repite es: {moda_notas}")
    # Si no hay moda, se lanza una StatisticsError
    except StatisticsError:
        print("No se pudo determinar la moda.")
    print(50*"*")

#4. Que porcentaje de estudiantes tiene al menos una nota bajo 4.0?
def calcular_porcentaje_cuatro(estudiantes):
    cantidad_de_estudiantes = len(estudiantes)
    """any() devuelve True si encuentra al menos una nota bajo 4.0,
    y False en caso contrario."""
    estudiantes_bajo_cuatro = sum(1 for estudiante in estudiantes if any(nota < 4.0 for nota in estudiante["notas"])) 
    porcentaje = (estudiantes_bajo_cuatro / cantidad_de_estudiantes) * 100
    print(f"Porcentaje de estudiantes con al menos una nota bajo 4.0: {porcentaje:.2f}%")
    print(50*"*")

#5. entrega un listado ordenado (de mayor a menor) de los estudiantes segun su promedio. 
def listado_estudiantes_promedio(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x:x["promedio"], reverse=True)
    print("Listado de estudiantes ordenados por promedio (de mayor a menor):")
    for estudiante in estudiantes_ordenados:
        print(f"{estudiante['nombre']}: {estudiante['promedio']}")
    print(50*"*")





calcular_promedio(estudiantes)
aprobados(estudiantes)
moda(estudiantes)
calcular_porcentaje_cuatro(estudiantes)
listado_estudiantes_promedio(estudiantes)
