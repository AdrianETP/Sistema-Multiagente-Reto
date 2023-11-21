import matplotlib.animation as animation
import random
import ciudad
import estacion
import pasajero
import tren
import matplotlib.pyplot as plt

cm = ciudad.Ciudad([1 , 5 , 8], 1000, [60 for i in range(0, 3)])
cm.step() # funcion para el api

dc = cm.datacollector.get_model_vars_dataframe()

fig, axs = plt.subplots(figsize=(7, 7))

patch = plt.imshow(dc.iloc[0][0], cmap=plt.cm.binary)


def animate(i):
    patch.set_data(dc.iloc[i][0])


anim = animation.FuncAnimation(fig, animate, frames=len(dc))
# plt.show()
anim.save('animation.gif', fps = 30)
