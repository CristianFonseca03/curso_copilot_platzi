# Proyecto API en Python

Este proyecto es una API simple en Python construida utilizando Flask y Flasgger para la documentación de la API.

## Requisitos

- Python 3.12 o superior
- Flask
- Flasgger

## Configuración y Activación

1. Clona el repositorio:
   ```bash
   git clone <repository-url>
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd PythonAPI
   ```

3. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   ```

4. Activa el entorno virtual:
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```cmd
     venv\Scripts\activate
     ```

5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecutando la API

1. Inicia la aplicación Flask:
   ```bash
   python app.py
   ```

2. Abre tu navegador y navega a:
   ```
   http://127.0.0.1:5000/saludo?cadenadeentrada=TuNombre
   ```
   Reemplaza `TuNombre` con el texto que desees.

## Documentación de la API

La documentación de la API está disponible en:
```
http://127.0.0.1:5000/apidocs/
```

## Pruebas Unitarias

Se han agregado pruebas unitarias para la API utilizando el módulo `unittest`. Para ejecutarlas, sigue estos pasos:

1. Asegúrate de que el entorno virtual esté activado.
2. Ejecuta las pruebas con el siguiente comando:
   ```bash
   python -m unittest test_app.py
   ```

Esto ejecutará las pruebas definidas en el archivo `test_app.py` y mostrará los resultados en la terminal.

## Notas

- Asegúrate de que `pip` esté instalado en tu sistema. Si no lo está, instálalo usando:
  ```bash
  sudo apt install python3-pip
  ```