# Mapa Visual de Algoritmos y Estructuras de Datos

```
                                ESTRUCTURAS DE DATOS FUNDAMENTALES
┌───────────────────┬────────────────────┬─────────────────┬──────────────────┬────────────────┐
│      Arrays       │    Hash Tables     │     Stacks      │      Queues      │   Linked Lists  │
└─────────┬─────────┴──────────┬─────────┴────────┬────────┴────────┬─────────┴────────┬───────┘
          │                    │                  │                  │                  │
          ▼                    ▼                  ▼                  ▼                  ▼
┌─────────────────┐  ┌──────────────────┐ ┌────────────────┐ ┌─────────────────┐ ┌────────────────┐
│  • Two Pointers │  │• Mapeo de valores│ │• Valid brackets│ │ • BFS           │ │• Runner técnica│
│  • Binary Search│  │• Contar frec.    │ │• Historial     │ │ • Level order   │ │• Ciclos        │
│  • Sliding Window│ │• Two Sum         │ │• Evaluación    │ │ • Shortest path │ │• Reversal      │
└─────────────────┘  └──────────────────┘ └────────────────┘ └─────────────────┘ └────────────────┘

                              ESTRUCTURAS DE DATOS AVANZADAS
┌───────────────────┬────────────────────┬─────────────────┬──────────────────┐
│      Trees        │       Heaps        │     Tries       │      Graphs      │
└─────────┬─────────┴──────────┬─────────┴────────┬────────┴────────┬─────────┘
          │                    │                  │                  │
          ▼                    ▼                  ▼                  ▼
┌─────────────────┐  ┌──────────────────┐ ┌────────────────┐ ┌─────────────────────┐
│ • DFS (preorder,│  │• Top K elementos │ │• Prefijo común │ │• DFS/BFS            │
│   inorder,      │  │• Kth smallest    │ │• Autocomplete  │ │• Dijkstra           │
│   postorder)    │  │• Merge K sorted  │ │• Word search   │ │• Topological Sort   │
│ • Altura/Balance│  │• Median finding  │ │• Diccionarios  │ │• Connected components│
└─────────────────┘  └──────────────────┘ └────────────────┘ └─────────────────────┘

                                TÉCNICAS ALGORÍTMICAS
┌───────────────────┬────────────────────┬─────────────────┬──────────────────┐
│   Binary Search   │    Sliding Window  │   Two Pointers  │     Recursion    │
├───────────────────┼────────────────────┼─────────────────┼──────────────────┤
│ Dynamic Programming│      Greedy       │   Backtracking  │  Divide & Conquer │
└───────────────────┴────────────────────┴─────────────────┴──────────────────┘

                           TÉCNICAS + TIPOS DE PROBLEMAS
┌───────────────────────────────────────────────────────────────────────────────┐
│ • Binary Search → Búsqueda en arrays ordenados, encontrar puntos de inflexión │
│ • Sliding Window → Subarrays/subcadenas contiguos con propiedades            │
│ • Two Pointers → Pares que cumplen condiciones, subarrays                    │
│ • Dynamic Programming → Optimización con subproblemas superpuestos           │
│ • Greedy → Decisiones localmente óptimas                                     │
│ • Backtracking → Combinaciones, permutaciones, problemas de restricciones    │
│ • DFS/BFS → Exploración de árboles/grafos, caminos, conectividad             │
└───────────────────────────────────────────────────────────────────────────────┘

                           COMPLEJIDAD DE ALGORITMOS COMUNES
┌─────────────────┬────────────────┬───────────────────────────────────────────┐
│    Algoritmo    │   Complejidad  │               Aplicaciones                │
├─────────────────┼────────────────┼───────────────────────────────────────────┤
│ Binary Search   │    O(log n)    │ Búsqueda en colecciones ordenadas         │
│ Merge Sort      │   O(n log n)   │ Ordenamiento estable                      │
│ Quick Sort      │   O(n log n)   │ Ordenamiento eficiente (promedio)         │
│ DFS/BFS         │    O(V + E)    │ Recorrido de grafos/árboles               │
│ Dijkstra        │ O(E log V)     │ Caminos más cortos con pesos positivos    │
│ Sliding Window  │     O(n)       │ Subarrays con propiedades específicas     │
│ Dynamic Prog.   │ O(n²) o O(n·k) │ Problemas de optimización                 │
└─────────────────┴────────────────┴───────────────────────────────────────────┘
```

## Guía de Decisión: ¿Qué Algoritmo Usar?

```
¿Datos ordenados?
├── Sí → ¿Buscando elemento específico? → Binary Search
└── No → ¿Se pueden ordenar? → Sort + Binary Search

¿Trabajando con subarrays/subcadenas?
├── ¿Elementos contiguos? → Sliding Window
└── ¿Pares de elementos? → Two Pointers

¿Problema de optimización?
├── ¿Subproblemas superpuestos? → Dynamic Programming
└── ¿Decisiones locales óptimas? → Greedy

¿Buscando todas las combinaciones/permutaciones?
└── Backtracking

¿Estructura jerárquica?
├── Árboles → DFS/BFS, In/Pre/Post-order
└── Grafos → DFS, BFS, Dijkstra, Topological Sort

¿Encontrar Top K elementos?
└── Heap

¿Búsqueda de prefijos o palabras?
└── Trie

¿Validación de expresiones?
└── Stack

¿Procesamiento por niveles/orden?
└── Queue + BFS
```