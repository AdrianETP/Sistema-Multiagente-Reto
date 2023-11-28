import matplotlib.animation as animation
import random
import ciudad
import estacion
import pasajero
import tren
import InicializadorModelo
import matplotlib.pyplot as plt

# Ejecución del modelo de simulación 2000 veces
for i in range(2000):
    InicializadorModelo.cm.step()  # funcion para el api

# Imprimir el número de pasajeros no satisfechos después de la simulación
print("hubo ", InicializadorModelo.cm.pasajeros_no_satisfechos, "pasajeros no satisfechos")
# Recopilación de los datos generados por la simulación
dc = InicializadorModelo.cm.datacollector.get_model_vars_dataframe()

# Configuración de la figura para la animación
fig, axs = plt.subplots(figsize=(7, 7))

# Visualización inicial de los datos de la simulación
patch = plt.imshow(dc.iloc[0][0], cmap=plt.cm.binary)

# Definición de la función de animación que actualiza la visualización en cada cuadro
def animate(i):
    patch.set_data(dc.iloc[i][0])


anim = animation.FuncAnimation(fig, animate, frames=len(dc))
# plt.show()
anim.save("animation.gif", fps=30)
