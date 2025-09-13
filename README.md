# Registro de Temperaturas

Este proyecto contiene un script en Python para calcular la **temperatura promedio** de varias ciudades a lo largo de varias semanas.

## 📌 Funcionalidad
La función `calcular_promedios(datos)` recibe un diccionario con los nombres de las ciudades como claves y una lista de temperaturas como valores. Retorna un diccionario con el promedio de cada ciudad.

### Ejemplo de entrada:
```python
datos_temperaturas = {
    "Guaranda": [20, 22, 19, 21],
    "Quito": [15, 16, 14, 17],
    "Ambato": [18, 19, 20, 21]
}
```

### Ejemplo de salida:
```
Promedios de temperatura por ciudad:
Guaranda: 20.5 °C
Quito: 15.5 °C
Ambato: 19.5 °C
```

## 🚀 Uso
1. Clona este repositorio:
   ```bash
   git clone https://github.com/MayraMoran/Registro-temperatura.git
   cd Registro-temperatura
   ```

2. Ejecuta el script:
   ```bash
   python temperaturas.py
   ```

## 📝 Autor
- **Mayra Morán**  
Carrera de Pedagogía de la Matemática y la Física  
Universidad Estatal de Bolívar  
