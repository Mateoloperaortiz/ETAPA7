# ETAPA 7
## Algoritmo Dijkstra
Dada una matriz de adyacencia (la cual será solicitada al usuario para que la ingrese en tiempo de ejecución), un punto de inicio y un punto final, encontrar el camino más corto usando el algoritmo de Dijkstra y presentar el recorrido entre los nodos que hacen parte del camino óptimo.


**Explicación del código:**

1. **Importación del módulo sys:**

   ```python
   import sys
   ```

   - Se importa el módulo `sys` para utilizar `sys.maxsize`, que proporciona el valor entero más grande soportado por el sistema. Esto es útil para inicializar las distancias con un valor que represente "infinito".

2. **Definición de la función `dijkstra`:**

   ```python
   def dijkstra(graph, start, end):
   ```

   - La función `dijkstra` recibe tres parámetros:
     - `graph`: La matriz de adyacencia que representa el grafo.
     - `start`: El nodo inicial desde donde se calcularán las distancias.
     - `end`: El nodo final al que se desea encontrar el camino más corto.

3. **Inicialización de variables:**

   ```python
   n = len(graph)
   visited = [False] * n
   distance = [sys.maxsize] * n
   previous = [None] * n
   ```

   - `n`: Número de nodos en el grafo.
   - `visited`: Lista booleana que indica si un nodo ha sido visitado. Inicialmente, todos los nodos están sin visitar (`False`).
   - `distance`: Lista que almacena la distancia mínima conocida desde el nodo inicial a cada nodo. Se inicializa con "infinito" (`sys.maxsize`) para todos los nodos excepto el inicial.
   - `previous`: Lista que almacena el predecesor de cada nodo en el camino más corto encontrado. Se utiliza para reconstruir el camino al final.

4. **Establecer la distancia al nodo inicial:**

   ```python
   distance[start] = 0
   ```

   - La distancia desde el nodo inicial a sí mismo es 0, ya que no hay desplazamiento.

5. **Algoritmo principal de Dijkstra:**

   ```python
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
   ```

   - **Bucle principal:**
     - Se repite `n` veces para asegurarse de que todos los nodos sean procesados.
   - **Encontrar el nodo no visitado con la distancia mínima:**
     - Se inicializan `min_distance` y `min_index` para encontrar el nodo con la menor distancia que aún no ha sido visitado.
     - Se recorre la lista de distancias y se actualiza `min_distance` y `min_index` cuando se encuentra un nodo con una distancia menor.
   - **Verificar si todos los nodos accesibles han sido visitados:**
     - Si `min_index` sigue siendo `-1`, significa que no hay más nodos alcanzables desde el nodo inicial, y se rompe el bucle.
   - **Marcar el nodo seleccionado como visitado:**
     - `visited[min_index] = True`
   - **Actualizar las distancias a los nodos adyacentes:**
     - Se recorre la fila correspondiente al nodo `min_index` en la matriz de adyacencia.
     - Si existe una arista (`graph[min_index][i] != 0`) y el nodo `i` no ha sido visitado:
       - Se calcula la nueva distancia potencial `new_dist`.
       - Si `new_dist` es menor que la distancia conocida `distance[i]`, se actualiza `distance[i]` y se establece `previous[i]` como `min_index`.

6. **Reconstruir el camino más corto:**

   ```python
   path = []
   current = end
   while current is not None:
       path.insert(0, current)
       current = previous[current]
   ```

   - Se crea una lista `path` vacía.
   - Se inicia desde el nodo final y se sigue hacia atrás utilizando la lista `previous` hasta llegar al nodo inicial.
   - Se inserta cada nodo al inicio de la lista `path` para que el camino quede en orden desde el inicio hasta el final.

7. **Mostrar el resultado:**

   ```python
   if distance[end] == sys.maxsize:
       print("No hay camino desde el nodo {} al nodo {}".format(start, end))
   else:
       print("La distancia más corta desde el nodo {} al nodo {} es {}".format(start, end, distance[end]))
       print("El camino es: {}".format(" -> ".join(map(str, path))))
   ```

   - Si la distancia al nodo final es "infinito", significa que no hay camino desde el nodo inicial al nodo final.
   - De lo contrario, se imprime la distancia más corta y el camino encontrado.

8. **Función principal `main`:**

   ```python
   def main():
       n = int(input("Ingrese el número de nodos: "))
       print("Ingrese la matriz de adyacencia (use 0 para indicar ausencia de conexión):")
       graph = []
       for i in range(n):
           row = list(map(int, input().split()))
           graph.append(row)
       start = int(input("Ingrese el nodo inicial (0 a {}): ".format(n - 1)))
       end = int(input("Ingrese el nodo final (0 a {}): ".format(n - 1)))
       dijkstra(graph, start, end)
   ```

   - **Entrada del número de nodos:**
     - Solicita al usuario ingresar el número de nodos del grafo.
   - **Entrada de la matriz de adyacencia:**
     - Informa al usuario que ingrese la matriz de adyacencia, utilizando `0` para indicar que no hay conexión directa entre dos nodos.
     - Se utiliza un bucle para leer cada fila de la matriz.
     - Convierte la entrada del usuario en una lista de enteros y la agrega a la matriz `graph`.
   - **Entrada del nodo inicial y final:**
     - Solicita al usuario que ingrese el nodo inicial y el nodo final, asegurándose de que estén dentro del rango válido (`0` a `n - 1`).
   - **Llamada a la función `dijkstra`:**
     - Ejecuta el algoritmo de Dijkstra con los datos proporcionados.

9. **Ejecución del programa:**

   ```python
   if __name__ == "__main__":
       main()
   ```

   - Esta condición verifica si el script se está ejecutando directamente (no importado como módulo).
   - Si es así, llama a la función `main()` para iniciar el programa.

**Cómo funciona el programa en conjunto:**

- El programa solicita al usuario la información necesaria para construir el grafo y especificar los nodos de inicio y fin.
- Utiliza el algoritmo de Dijkstra para calcular el camino más corto entre el nodo inicial y el nodo final.
- Imprime la distancia mínima y el camino recorrido.

**Ejemplo de ejecución:**

```
Ingrese el número de nodos: 5
Ingrese la matriz de adyacencia (use 0 para indicar ausencia de conexión):
0 10 0 30 100
10 0 50 0 0
0 50 0 20 10
30 0 20 0 60
100 0 10 60 0
Ingrese el nodo inicial (0 a 4): 0
Ingrese el nodo final (0 a 4): 4
```

**Salida:**

```
La distancia más corta desde el nodo 0 al nodo 4 es 60
El camino es: 0 -> 3 -> 2 -> 4
```