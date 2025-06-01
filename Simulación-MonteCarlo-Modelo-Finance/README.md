# Simulador de Monte Carlo para Modelo Financiero 📊

Este proyecto reproduce una funcionalidad clave del software **Crystal Ball**: simular escenarios financieros bajo incertidumbre para evaluar la distribución del Valor Presente Neto (NPV) de un modelo desarrollado en Excel. Utiliza Python y Excel en conjunto para realizar simulaciones tipo Monte Carlo, graficar los resultados y exportarlos.
Este desarrollo fue parte de un ejercicio académico para un caso de estudio en el curso **Finance 1**.

---

## 🧠 ¿Qué hace este proyecto?

1. **Conecta con un archivo de Excel** que contiene un modelo financiero.
2. **Simula 5000 escenarios aleatorios** para variables críticas (crecimiento de ventas, costos y tasa impositiva).
3. **Calcula el NPV en cada escenario**, leyendo automáticamente desde Excel.
4. **Guarda los resultados** en un archivo `.npy`.
5. **Visualiza la distribución de los NPVs**:
   - Histograma estático (`PNG`)
   - Histograma animado (`GIF`)

---

## 📂 Archivos

- `simulacion_excel.py`: script principal que corre la simulación de Monte Carlo directamente sobre el archivo de Excel.
- `visualizacion_histogramas.py`: script que genera las visualizaciones estáticas y animadas de la distribución del NPV.
- `npvs.npy`: archivo generado automáticamente con los resultados de las simulaciones (requiere correr el script).
- **Requiere** el archivo Excel del modelo (`Sport limited final.xlsx`) con hoja `Escenarios` y valores clave en las celdas `I5`, `I6`, `I13` y `C203`.
-   ⚠️ *Este ultimo archivo de Excel no es de mi autoría, por lo que **no está incluido** en el repositorio por razones de propiedad intelectual.*


---

## 🛠️ Requisitos

- Python 3.x
- [xlwings](https://pypi.org/project/xlwings/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- `numpy`
- Excel instalado en el sistema

Instalación:
```bash
py -m pip install xlwings matplotlib numpy
```

---

## 🔍 ¿Cómo funciona?

### 1. `simulacion_excel.py`

- Ejecuta 5000 simulaciones de Monte Carlo
- Modifica directamente celdas del Excel
- Lee el resultado del NPV final y lo guarda en `npvs.npy`

### 2. `visualizacion_histogramas.py`

- Carga el archivo `npvs.npy`
- Genera un histograma estático (`PNG`)
- Crea un GIF animado mostrando cómo se va formando la distribución

---

## 📈 Resultados esperados

Después de ejecutar ambos scripts, obtendrás:
- Un archivo `npvs.npy` con todos los valores simulados.
- Una imagen `histograma_npv.png` con la distribución final.
- Una animación `histograma_npv.gif` mostrando cómo se forma la distribución paso a paso.

---

## ⚠️ Notas

- Asegúrate de tener el archivo Excel en la ruta correcta con los rangos mencionados.
- El código accede directamente a Excel, por lo que **no funciona en plataformas sin Excel (Linux, macOS sin Office)**.
- Puedes ajustar el número de simulaciones o el rango de variación de las variables en el script.

---

Hecho con 🧪 por César Vargas 2025
