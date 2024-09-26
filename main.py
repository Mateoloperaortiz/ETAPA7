import sys  # Importa el módulo sys para acceder a sys.maxsize, que representa el valor máximo de un entero.

def dijkstra(graph, start, end):
    n = len(graph)  # Obtiene el número de nodos en el grafo.
    visited = [False] * n  # Crea una lista para marcar si un nodo ha sido visitado.
    distance = [sys.maxsize] * n  # Inicializa las distancias con un valor muy grande (infinito).
    previous = [None] * n  # Almacena el predecesor de cada nodo en el camino más corto.

    distance[start] = 0  # La distancia desde el nodo inicial a sí mismo es 0.

    # Itera n veces para visitar todos los nodos.
    for _ in range(n):
        # Inicializa la distancia mínima y el índice del nodo con la distancia mínima.
        min_distance = sys.maxsize
        min_index = -1

        # Busca el nodo no visitado con la distancia mínima.
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]  # Actualiza la distancia mínima.
                min_index = i  # Actualiza el índice del nodo con la distancia mínima.

        # Si no se encuentra un nodo no visitado, se rompe el bucle (el grafo puede no ser completamente conectado).
        if min_index == -1:
            break

        visited[min_index] = True

        for i in range(n):
            if graph[min_index][i] != 0 and not visited[i]:
                new_dist = distance[min_index] + graph[min_index][i]
                if new_dist < distance[i]:
                    distance[i] = new_dist
                    previous[i] = min_index

    # Reconstruir el camino
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    if distance[end] == sys.maxsize:
        print("No hay camino desde el nodo {} al nodo {}".format(start, end))
    else:
        print("La distancia más corta desde el nodo {} al nodo {} es {}".format(start, end, distance[end]))
        print("El camino es: {}".format(" -> ".join(map(str, path))))

def main():
    n = int(input("Ingrese el número de nodos: "))
    print("Ingrese la matriz de adyacencia (use 0 para indicar ausencia de conexión):")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    start = int(input("Ingrese el nodo inicial (0 a {}): ".format(n-1)))
    end = int(input("Ingrese el nodo final (0 a {}): ".format(n-1)))
    dijkstra(graph, start, end)

if __name__ == "__main__":
    main()
