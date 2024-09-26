import sys

def dijkstra(graph, start, end):
    n = len(graph)
    visited = [False]*n
    distance = [sys.maxsize]*n
    previous = [None]*n

    distance[start] = 0

    for _ in range(n):
        # Encontrar el nodo no visitado con la distancia más pequeña
        min_distance = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

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
