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





class Ciudad(Model):
    def __init__(self, ubicaciones_estaciones, numero_personas, tiempos):
        super().__init__()
        self.grid = MultiGrid(140, 21, True)
        self.height = 140
        self.width = 21
        self.ids = []
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

        # estaciones
        for i in range(0, len(self.ubicaciones_estaciones)):
            for k in range(0, 9):
                for j in range(0, 10):
                    possible_id = random.random()
                    while possible_id in self.ids:
                        possible_id = random.random()
                    self.ids.append(possible_id)
                    estacion_temp = estacion.Estacion_Tren(
                        possible_id,
                        i,
                        self.ubicaciones_estaciones[i],
                        tiempos[i],
                        self,
                    )
                    self.estaciones.append(estacion_temp)

                    self.grid.place_agent(
                        estacion_temp,
                        (j + (self.ubicaciones_estaciones[i] * 15), k + 12),
                    )

        # creacion del tren
        
        for i in range(10):
            possible_id = random.random()
            while possible_id in self.ids:
                possible_id = random.random()
            self.ids.append(possible_id)
            tren_temp = tren.Tren(possible_id, self, 0 , i)
            self.tren = tren_temp
            self.schedule.add(tren_temp)
            self.grid.place_agent(tren_temp, (i, 11))
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




    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()