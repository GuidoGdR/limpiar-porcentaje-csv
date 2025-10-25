# 🧹 `limpiar-porcentaje-csv` - Limpiador de Porcentajes CSV

**Script diseñado para limpiar un archivo CSV, eliminando el símbolo de porcentaje (`%`) de los números y dividiendo el valor resultante por 100.**

---

## ⚙️ Funcionamiento

Este script automatiza la transformación de datos para facilitar el cálculo.

### 🔄 Proceso de Limpieza

1.  **Identificación:** Busca en el archivo de origen todos los valores que contengan el símbolo `%`.
2.  **Limpieza:** Elimina el símbolo `%`.
3.  **Conversión:** Divide el número resultante por **100** (convirtiéndolo de valor porcentual a valor decimal).

> **Ejemplo:** Un valor de `"15%"` se convierte en `0.15`.

---

## 📂 Archivos Necesarios

Para la ejecución, el script utiliza y genera los siguientes archivos en el directorio de trabajo:

| Archivo | Función |
| :--- | :--- |
| **`Archivo_a_limpiar.csv`** | **Entrada:** Contiene los datos originales que necesitan la limpieza de porcentajes. |
| **`Archivo_limpio.csv`** | **Salida:** Archivo nuevo donde se pega la información con los porcentajes ya transformados a valores decimales. |

---

## 🚀 Uso

Simplemente asegúrate de que el archivo de entrada (`Archivo_a_limpiar.csv`) se encuentre en la ubicación correcta y ejecuta el script.
