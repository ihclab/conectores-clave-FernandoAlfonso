# imprimir bonito:
import pprint

# Visualización:
import matplotlib.pyplot as plt
import networkx as nx

# Crear usuarios:
users = [
	{"id": 0, "name": "Hero" },
	{"id": 1, "name": "Dunn" },
	{"id": 2, "name": "Sue" },
	{"id": 3, "name": "Chi" },
	{"id": 4, "name": "Thor" },
	{"id": 5, "name": "Clive" },
	{"id": 6, "name": "Hicks" },
	{"id": 7, "name": "Devin" },
	{"id": 8, "name": "Kate" },
	{"id": 9, "name": "Klein" }
]

# Crear friendships:
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Agregar atributo friends a users:
for user in users:
	user ['friends'] = []
	

# Agregar amigos relacionados (visualización):
relaciones = []

# Obtener relaciones de cada usuario:
for x,y in friendships:
	users [x] ['friends'].append (users [y] ['name'])
	users [y] ['friends'].append (users [x] ['name'])

	# Para la visualización:
	relaciones.append((users [x] ['name'],users [y] ['name']))
	relaciones.append((users [y] ['name'],users [x] ['name']))

# ¿Cuál es el número promedio de conexiones?:
	conexiones = []

	def promedio ():
		# Paso 1, contar y sumar las conexion de cada usuario:
		suma = 0

		for user in users:
			# total de conexiones:
			noConexiones = len(user ['friends'])

			# Sumar conexiones de todos los usuarios: 
			suma += noConexiones

			# Agregar número de conexiones para poder ordenar:
			user ['noConexiones'] = noConexiones

			# Total de conexiones para el tamaño de los círculo en la visualización:
			conexiones.append (noConexiones * 700)

		# Paso 2 dividir el total de las sumas entre el total de  usuarios (promedio)
		print(f"promedio: {suma / len (users)}")

# ¿Quiénes son los más conectados (mayor número de amigos)? Ordenarlos de mayor a menor.
	# Después de que los datos están ordenados de menor a mayor, los ordena a la inversa:
	def ordenarMayorMenor (datos):
		noDatos = len(datos)
		datos2 = []

		for i in range(noDatos-1,-1,-1):
			datos2.append (datos [i])

		return datos2

	# Método de ordenamiento (los ordena de menor a mayor)
	def quicksort (datos):
		if len(datos) < 1:
			return []
		
		leftElements = []
		rightElements = []
		pivote = datos [0] ['noConexiones']

		for i in range(1,len (datos)):
			if datos [i] ['noConexiones'] < pivote:
				leftElements.append (datos [i])
			else:
				rightElements.append (datos [i])

		return quicksort (leftElements) + [datos [0]] + quicksort (rightElements)


# Resultados
promedio()

resultado = ordenarMayorMenor(quicksort(users))
pprint.pprint(resultado)


# Visualización:
# Inicializar objeto para graficar:
G = nx.Graph()

# Agregar relaciones a graficar:
G.add_edges_from(relaciones)

# Dibujar configurando parámetros:
nx.draw(G, node_size=conexiones, with_labels=True)

# mostrar lo graficado
plt.show()