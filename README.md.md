# Registro de Temperaturas y Cálculo de Descuento

Este repositorio contiene dos programas en Python:

1. **temperaturas.py** → Calcula el promedio de temperaturas de varias ciudades durante varias semanas.
2. **CalculoDescuentoPython.py** → Calcula el descuento aplicado en una compra según el porcentaje indicado.

---

## 📌 Funcionalidad

### 1. temperaturas.py
La función `calcular_promedios(datos)` recibe un diccionario con nombres de ciudades y listas de temperaturas.  
Devuelve un diccionario con el promedio de cada ciudad.

#### Ejemplo de entrada:
```python
datos_temperaturas = {
    "Guaranda": [20, 22, 19, 21],
    "Quito": [15, 16, 14, 17],
    "Ambato": [18, 19, 20, 21]
}
```

#### Ejemplo de salida:
```
Promedios de temperatura por ciudad:
Guaranda: 20.5 °C
Quito: 15.5 °C
Ambato: 19.5 °C
```

### 2. CalculoDescuentoPython.py
La función `calcular_descuento(monto_total, porcentaje_descuento=10)` calcula el descuento en función del monto de la compra y el porcentaje indicado (10% por defecto).

#### Ejemplo de salida:
```
Compra 1:
  Monto total: $100.0
  Descuento aplicado (10%): $10.0
  Monto final a pagar: $90.0

Compra 2:
  Monto total: $200.0
  Descuento aplicado (20%): $40.0
  Monto final a pagar: $160.0
```

---

## 🚀 Uso
1. Clona este repositorio:
   ```bash
   git clone https://github.com/MayraMoran/Registro-temperatura.git
   cd Registro-temperatura
   ```

2. Ejecuta los programas:
   ```bash
   python temperaturas.py
   python CalculoDescuentoPython.py
   ```

---

## 📝 Autor
- **Mayra Morán**  
Carrera de Tecnologias de la información 
Universidad Estatal Amazonica  
