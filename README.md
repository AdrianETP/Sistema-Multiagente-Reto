# Sistema-Multiagente-Reto

- Este es un sistema multiagentes simulando las estaciones de la linea 5


## Como Preparar tu simulacion

para preparar la simulacion, abre el archivo __InicializadorModelo.py__ y modifica la variable cm para adaptar tu simulacion.

```python
poblacion_estaciones = [
    (0, 11),
    (1, 20),
    (2, 18),
    (3, 21),
    (4, 4),
    (5, 5),
    (6, 4),
    (7, 11),
    (8, 2),
]

cm = ciudad.Ciudad(
    [poblacion_estaciones[1], poblacion_estaciones[5], poblacion_estaciones[7]], # estaciones que se van a usar
    1000, # numero de pasajeros
    [random.randrange(10, 60, 10) for i in range(0, 3)], # tiempos por cada estacion
)


```

## Como correr tu simulacion

### como gif

para correr la simulacion como GIF, corre el siguiente comando en la terminal

```bash
python3 .
```
esto generara un gif (_que se tarda en crear_) el cual visualiza la simulacion del tren


### como API

para correr el codigo como API, corre el siguiente codigo en la terminal

```bash
python3 api.py
```

esto generara una api local en el puerto 5000, la cual al llamarla te dara toda la informacion de la simulacion
  - por cada llamada genera un step nuevo
