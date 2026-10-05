# infra-equipo

Repositorio de infraestructura del laboratorio de Administración de Centros de Cómputo (Semana 08 – Git, GitHub y DevOps).

## Descripción
Despliegue con Docker Compose de Nginx y Apache httpd sirviendo una página web propia, más un script en Python que genera un reporte del sistema.

## Estructura
    infra-equipo/
    ├── docker-compose.yml     # servicios nginx y apache
    ├── .env.example           # variables de ejemplo (puertos)
    ├── .gitignore             # evita subir secretos
    ├── web/index.html         # página web que sirven ambos servidores
    ├── scripts/reporte_sistema.py
    └── notas-miguel.md

## Requisitos
- Ubuntu/Debian con Docker y Docker Compose
- Python 3
- Git y acceso SSH a GitHub

## Cómo desplegar
    git clone git@github.com:miguelst856-art/infra-equipo.git
    cd infra-equipo
    cp .env.example .env
    sudo docker compose up -d

- Nginx: http://IP_DEL_SERVIDOR:8080
- Apache: http://IP_DEL_SERVIDOR:8081

## Reporte del sistema
    python3 scripts/reporte_sistema.py

## Buenas prácticas
- Nunca subir `.env`, claves privadas ni contraseñas (ver `.gitignore`).
- Un commit pequeño con mensaje claro por cada cambio.
- Trabajar en ramas y fusionar a `main` cuando funciona.

## Integrantes
- Miguel Saldaña
