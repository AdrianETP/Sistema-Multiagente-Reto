from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import estacion
import tren
from mesa.time import RandomActivation
import random
import pasajero

def get_grid(model):
    grid = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, (x, y) = cell
        for obj in cell_content:
            if isinstance(obj, estacion.Estacion_Tren):
                grid[x][y] = 1
            if isinstance(obj, tren.Tren):
                grid[x][y] = 2
            if isinstance(obj , pasajero.Pasajero):
                grid[x][y] = 3
    return grid


def get_model_state(model):
    # Recopila datos de los agentes para convertirlos en un objeto que puede ser JSON serializable
    model_state = {

        "tren": {
            "id": model.tren.id,
            "pasajeros": model.tren.pasengers,
            "limit": model.tren.limit,
            "doors": model.tren.doors,
            "position": model.tren.pos,
            "timer": model.tren.timer,
        },
        # Cada estacion mide 10x10, entre cada estacion hay 5 de espacio
        "estaciones": [(estacion * 15, 12) for estacion in model.ubicaciones_estaciones], #arrojja las posicones (y, x)
        "pasajeros": [
            {
            "id": pasajero.unique_id,
            "posicion": pasajero.pos,
            "satisfaccion": pasajero.satisfaccion, # Si NO tiene un destino por lo tanto es nulo
            "ubicacion": pasajero.ubicacion, # Cuando un agente sube al tren su estacion se vuleve nula

            
            "en_tren": pasajero.in_train
        }
        for pasajero in model.pasajeros
        ]
        

    }
    return model_state


class Ciudad(Model): 
    def __init__(self, ubicaciones_estaciones, numero_personas, tiempos):
        super().__init__()
        self.grid = MultiGrid(140, 21, True)
        self.height = 140
        self.width = 21
        self.ids = []
        self.pasajeros = []
        self.pasajeros_no_satisfechos = 0
        self.posibles_ubicaciones = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ]  # Tec , estanzuela, centro
        self.ubicaciones_estaciones = ubicaciones_estaciones
        self.numero_personas = numero_personas
        self.schedule = RandomActivation(self)
        self.estaciones = []

        # creacion de agentes

        # Creación de estaciones
        for i, ubicacion in enumerate(self.ubicaciones_estaciones):
            possible_id = random.random()
            while possible_id in self.ids:
                possible_id = random.random()
            self.ids.append(possible_id)
            estacion_temp = estacion.Estacion_Tren(
                possible_id,
                i,
                ubicacion,
                tiempos[i],
                self,
            )
            self.estaciones.append(estacion_temp)
            # Coloca la estación en la ubicación correspondiente en la grilla
            self.grid.place_agent(estacion_temp, (ubicacion * 15, 12))  # Ajusta las coordenadas según sea necesario

        # Creación del tren
        possible_id = random.random()
        while possible_id in self.ids:
            possible_id = random.random()
        self.ids.append(possible_id)
        self.tren = tren.Tren(possible_id, self, 0, 0)  # El tren tendrá un id y una posición inicial
        self.schedule.add(self.tren)
        self.grid.place_agent(self.tren, (0, 11))  # Ajusta las coordenadas según sea necesario
        self.datacollector = DataCollector(model_reporters={"Grid": get_grid})

        # pasajeros
        for i in range(0, numero_personas):
            possible_id = random.random()
            while possible_id in self.ids:
                possible_id = random.random()
            self.ids.append(possible_id)
            ubicacion = self.ubicaciones_estaciones[random.randrange(0 , len(self.ubicaciones_estaciones))]
            destino = self.posibles_ubicaciones[random.randrange(0 , len(self.posibles_ubicaciones))]
            while ubicacion == destino:
                destino = self.posibles_ubicaciones[random.randrange(0 , len(self.posibles_ubicaciones))]

            pasajero_temp = pasajero.Pasajero(possible_id , self , ubicacion=ubicacion,  destino=destino  )
            self.schedule.add(pasajero_temp)
            self.grid.place_agent(pasajero_temp, (pasajero_temp.ubicacion*(15) + random.randrange(0 , 10), random.randrange(12 , 21)))
            self.pasajeros.append(pasajero_temp)


    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()