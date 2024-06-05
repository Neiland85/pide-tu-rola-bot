# PideTuRolaBOT

PideTuRolaBOT es un sistema de gestión de peticiones de canciones para eventos como bodas, diseñado para mejorar la experiencia del DJ y los asistentes.

## Características

- Gestión de eventos y peticiones de canciones.
- Interfaz para agregar y listar peticiones de canciones.
- Manejo de múltiples eventos.

## Requisitos Previos

- Python 3.7 o superior
- Virtualenv

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/pide-tu-rola-bot.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd pide-tu-rola-bot
    ```
3. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
5. Configura las variables de entorno:
    - Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:
      ```env
      SECRET_KEY=tu-clave-secreta
      DATABASE_URL=sqlite:///site.db
      ```

## Uso

1. Inicia la aplicación:
    ```sh
    python run.py
    ```
2. La aplicación estará disponible en `http://127.0.0.1:5000/`.

## API Endpoints

### Peticiones de Canciones

- **Agregar una petición de canción**
  - **URL:** `/requests`
  - **Método:** `POST`
  - **Cuerpo:**
    ```json
    {
      "song_name": "Nombre de la canción",
      "artist": "Artista",
      "requested_by": "Solicitante",
      "event_id": 1
    }
    ```

- **Obtener peticiones de canciones por evento**
  - **URL:** `/requests/<int:event_id>`
  - **Método:** `GET`

### Eventos

- **Agregar un evento**
  - **URL:** `/events`
  - **Método:** `POST`
  - **Cuerpo:**
    ```json
    {
      "name": "Nombre del evento",
      "date": "2023-01-01T00:00:00",
      "location": "Ubicación"
    }
    ```

- **Obtener todos los eventos**
  - **URL:** `/events`
  - **Método:** `GET`

## Contribución

¡Contribuciones son bienvenidas! Por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Sube tus cambios a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Tu Nombre - Neil M [info@alquilerequipodesonido.com](www.alquilerequipodesonido.com)

Proyecto Link: [https://github.com/tu-usuario/pide-tu-rola-bot](https://github.com/tu-usuario/pide-tu-rola-bot)

