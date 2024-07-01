# Proyecto Unificado

Este proyecto es una aplicación web que utiliza Firebase Hosting para el despliegue y GitHub Actions para la integración continua.

## Funcionalidades

- Autenticación de usuarios
- Generación de códigos de barras SKU
- Almacenamiento y procesamiento de datos
- Integración con marketplaces
- Comparación de precios
- Optimización SEO

## Estructura del Proyecto

- `.dockerignore`: Lista de archivos y directorios que Docker debe ignorar.
- `.env`: Variables de entorno para la configuración del proyecto.
- `app.py`: Archivo principal de la aplicación Flask.
- `requirements.txt`: Lista de dependencias del proyecto.
- `Dockerfile`: Archivo de configuración de Docker.
- `scripts/`: Scripts adicionales para el proyecto.

## Despliegue

Este proyecto utiliza Firebase Hosting para el despliegue. Los cambios en la rama principal (`master`) activan automáticamente un flujo de trabajo de GitHub Actions que despliega la última versión de la aplicación.

## Configuración del Entorno

1. Clona el repositorio:

   ```bash
   git clone git@github.com:jrbarazone/unificado.git
   cd unificado
