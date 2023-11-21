from mesa import Model, Agent
class Tren(Agent):
    def __init__(self, unique_id, model, id, position):
        super().__init__(unique_id, model)
        self.pasengers = 0
        self.limit = 330
        self.doors = False  # cerradas: False, abiertas: True
        self.estacion = None
        self.id = id
        self.position = position
        self.timer = 0

    def step(self):
        
        # if self.pos[0] == self.model.height - self.position:
        #     return
        # else:
        if self.estacion == None:
            
            if (self.pos[0]-self.position) %15 == 0:
                
                # estacion ahora tiene un tren
                estacion = []
                for e in self.model.estaciones:
                    # 
                    if e.ubicacion == (self.pos[0]-self.position)/15:
                        estacion.append(e)
                if estacion != []:
                    self.estacion = estacion
                    self.timer =  self.estacion[0].tiempo
                    for e in self.estacion:
                        e.hay_tren = True
                    
                else:
                    self.model.grid.move_agent(self, (self.pos[0]+1, self.pos[1]))

            else:
                self.model.grid.move_agent(self, (self.pos[0]+1, self.pos[1]))
        else:
            if self.timer >0:
                
                
                self.timer -=1
                
            else:
                
                for e in self.estacion:
                    e.hay_tren = False
                self.estacion = None
                self.timer = 0
                self.model.grid.move_agent(self, (self.pos[0]+1, self.pos[1]))

