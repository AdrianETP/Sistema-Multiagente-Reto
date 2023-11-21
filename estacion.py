from mesa import Model, Agent
class Estacion_Tren(Agent):
    def __init__(self, unique_id, id, ubicacion, tiempo, model):
        super().__init__(unique_id=unique_id, model=model)
        self.ubicacion = ubicacion
        self.tiempo = tiempo
        self.hay_tren = False
        self.id = id
