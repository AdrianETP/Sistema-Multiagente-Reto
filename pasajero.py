from mesa import Model, Agent
import random
class Pasajero(Agent):
    def __init__(self, unique_id,  model, ubicacion, destino):
        super().__init__(unique_id, model)
        self.satisfaccion = 10
        self.ubicacion = ubicacion
        self.destino = destino
        self.in_train = False
        self.in_destino = False

    # funciones

    # moverse hacia las puertas
    # entrar al tren
    # modificar satisfaccion
    # salir del tren
    # satisfaccion 0

    def move(self):
        if self.destino == self.ubicacion:
            self.in_destino = True
        if self.in_destino == True:
            if self.pos[1] < 20:
                self.model.grid.move_agent(self, (self.pos[0] , self.pos[1]+1))
            return
        if self.in_train :
            if self.model.tren.estacion != None :
                self.ubicacion = self.model.tren.estacion[0].ubicacion
                
            if self.ubicacion == self.destino:
                self.model.grid.place_agent(self, (self.ubicacion*(15) , 12))
                self.model.tren.pasengers -=1
                self.in_destino = True
        else:
            if self.pos[0]-self.ubicacion*15 > 4:
                if self.pos[0] != self.ubicacion *15 +9:
                    self.model.grid.move_agent(self , (self.pos[0]+1, self.pos[1]))
                else:
                    if self.pos[1] != 12:
                        self.model.grid.move_agent(self, (self.pos[0] , self.pos[1]-1))
                    else:
                        if self.model.tren.pasengers != self.model.tren.limit:
                            # hacer que el pasajero se suba al tren (que desaparezca del grid)
                            self.model.tren.pasengers +=1
                            self.in_train = True
                            self.model.grid.remove_agent(self)
                        else:
                            self.subs_satisfaction()
                            self.model.grid.move_agent(self,(self.ubicacion*(15) + random.randrange(0 , 10), random.randrange(12 , 21)) )
            else:
                if self.pos [0] != self.ubicacion *15 :
                    self.model.grid.move_agent(self , (self.pos[0]-1, self.pos[1]))
                else:
                    if self.pos[1] != 12:
                        self.model.grid.move_agent(self, (self.pos[0] , self.pos[1]-1))
                    else:
                        if self.model.tren.pasengers != self.model.tren.limit:
                            # hacer que el pasajero se suba al tren (que desaparezca del grid)
                            self.model.tren.pasengers +=1
                            self.in_train = True
                            self.model.grid.remove_agent(self)
                        else:
                            self.subs_satisfaction()
                            self.model.grid.move_agent(self,(self.ubicacion*(15) + random.randrange(0 , 10), random.randrange(12 , 21)) )

    def subs_satisfaction(self):
        self.satisfaccion -= 2

    def satisfaccion_0(self):
        self.satisfaccion = 0

    def step(self):
        if self.destino not in self.model.ubicaciones_estaciones:
            self.satisfaccion_0()
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            return
        # buscar estacion
        # checar si este tiene trenes
            # si si tiene, correr mover haia las esquinas
        estacion = None
        for e in self.model.estaciones:
            if e.ubicacion == self.ubicacion:
                estacion = e
                break
        if estacion != None:
            if estacion.hay_tren == True or self.in_train:

                self.move()



