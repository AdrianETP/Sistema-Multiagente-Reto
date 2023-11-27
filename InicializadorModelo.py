import ciudad
import random

poblacion_estaciones = [(0, 11), (1, 20), (2, 18), (3, 21), (4, 4), (5, 5), (6, 4), (7, 11), (8, 2)]

cm = ciudad.Ciudad(
    [poblacion_estaciones[1], poblacion_estaciones[5], poblacion_estaciones[7]],
    1000,
    [random.randrange(10, 60, 10) for i in range(0, 3)],
)


