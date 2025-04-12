# GoAPI

GoAPI es un proyecto desarrollado en Go que proporciona una API para gestionar recursos. Este proyecto está diseñado como parte del curso de Copilot en Platzi.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

- [Go](https://golang.org/dl/) (versión 1.16 o superior)
- [Git](https://git-scm.com/)
- Un editor de texto o IDE como Visual Studio Code

## Instalación y ejecución

Sigue estos pasos para clonar y ejecutar el proyecto:

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd GoAPI
   ```

2. Instala las dependencias necesarias:
   ```bash
   go mod tidy
   ```

3. Ejecuta el servidor:
   ```bash
   go run main.go
   ```

4. La API estará disponible en `http://localhost:8080`.

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección de errores:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Descripción de los cambios"
   ```
4. Envía tus cambios al repositorio remoto:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un Pull Request.
