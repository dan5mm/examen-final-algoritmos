# Solicitar al usuario el nombre del estudiante y sus notas
nombre_estudiante = print("Ingrese el nombre del estudiante: ")
notas = []
for i in range(4):
    nota = float(input(f"Ingrese la nota {i + 1}: ")) #convertir a float
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Guardar los datos en el archivo "notas.txt"
with open("notas.txt", "a") as archivo: #faltaban comillas
    archivo.write(f"Nombre del estudiante: {nombre_estudiante}\n")
    archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
    archivo.write(f"Promedio: {promedio}\n\n") # archivo.write

print("Datos guardados en el archivo 'notas.txt'.") #en ves de write es print
