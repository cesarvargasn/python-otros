import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Ruta donde quieres guardar los archivos
ruta_descargas = r"C:/Users/cesar/Downloads/"

# Cargamos npvs guardado anteriormente
npvs = np.load(ruta_descargas + "npvs.npy")

# 1. Crear y guardar histograma animado
fig, ax = plt.subplots()
n_bins = 40
ax.set_xlim(np.min(npvs)-20, np.max(npvs)+20)
ax.set_ylim(0, 400)  # Subimos el techo
ax.set_xlabel('NPV por acción ($)')
ax.set_ylabel('Frecuencia')
ax.set_title('Distribución del NPV - Simulación Monte Carlo')

def animate_hist(i):
    ax.clear()
    datos = npvs[:int(len(npvs) * (i / 100))]
    counts, bins, patches = ax.hist(datos, bins=n_bins, edgecolor='black')
    ax.set_xlim(np.min(npvs)-20, np.max(npvs)+20)
    ax.set_ylim(0, 400)
    ax.set_xlabel('NPV por acción ($)')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Distribución del NPV - Simulación Monte Carlo')
    
    for bin_left, bin_right, patch in zip(bins[:-1], bins[1:], patches):
        if (bin_left + bin_right)/2 > 0:
            patch.set_facecolor('blue')   # 🔵 Ahora positivos azules
        else:
            patch.set_facecolor('red')    # 🔴 Ahora negativos rojos

ani = animation.FuncAnimation(fig, animate_hist, frames=100, interval=50)
ani.save(ruta_descargas + "histograma_npv.gif", writer='pillow')
plt.close()
print("✅ Histograma animado guardado como GIF.")

# 2. Crear y guardar histograma estático
fig_static, ax_static = plt.subplots()
counts, bins, patches = ax_static.hist(npvs, bins=n_bins, edgecolor='black')
ax_static.set_xlim(np.min(npvs)-20, np.max(npvs)+20)
ax_static.set_ylim(0, 400)
ax_static.set_xlabel('NPV por acción ($)')
ax_static.set_ylabel('Frecuencia')
ax_static.set_title('Distribución del NPV - Simulación Monte Carlo (Final)')

for bin_left, bin_right, patch in zip(bins[:-1], bins[1:], patches):
    if (bin_left + bin_right)/2 > 0:
        patch.set_facecolor('blue')   # 🔵 Positivos azules
    else:
        patch.set_facecolor('red')    # 🔴 Negativos rojos

plt.savefig(ruta_descargas + "histograma_npv.png", bbox_inches='tight')
plt.close()
print("✅ Histograma estático guardado como PNG.")

