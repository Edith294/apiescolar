# 🐍 API REST Escolar — Flask + PostgreSQL

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Swagger](https://img.shields.io/badge/Docs-Swagger-green)

API REST desarrollada con **Python Flask** y **PostgreSQL** para la gestión escolar de estudiantes, materias y calificaciones. Proyecto de la **Unidad 3 - Aplicaciones Web Orientadas a Servicios**.

---

## 📸 Capturas de pantalla

### Api Estudiante 
<img width="1916" height="1073" alt="image" src="https://github.com/user-attachments/assets/d265fe3c-d16f-4614-b0d4-24841c18fe57" />


![Swagger UI](screenshots/swagger.png)


<img width="1919" height="1034" alt="image" src="https://github.com/user-attachments/assets/a992b9e8-441c-4bcc-9357-044754a78e9a" />

<img width="1917" height="997" alt="image" src="https://github.com/user-attachments/assets/41521605-21a3-494f-8cb0-4cc6c8fb70e4" />

<img width="1919" height="999" alt="image" src="https://github.com/user-attachments/assets/c4e23b91-37e7-4922-9d54-3042dc5e7930" />
<img width="1797" height="627" alt="image" src="https://github.com/user-attachments/assets/71c0d3e3-8ee7-4cc9-9993-b29ffc46ca70" />

<img width="1844" height="896" alt="image" src="https://github.com/user-attachments/assets/266edb7b-e74b-4417-8002-ec954b35177f" />

<img width="1785" height="603" alt="image" src="https://github.com/user-attachments/assets/7970f6c5-f344-45dc-9210-f773b6cf5fa6" />

<img width="1819" height="956" alt="image" src="https://github.com/user-attachments/assets/fa9abb7b-35e8-46e4-a737-beaba1289c0b" />

---

## 📋 Descripción

Este proyecto implementa una API REST completa que permite:

- **CRUD de Estudiantes** — crear, leer, actualizar y eliminar registros con paginación y filtros
- **Materias y Calificaciones** — relaciones entre tablas con cálculo de kardex y estadísticas
- **Autenticación JWT** — registro, login y rutas protegidas con tokens
- **Documentación Swagger** — interfaz interactiva para probar todos los endpoints
- **Borrado lógico** — los registros nunca se eliminan físicamente de la base de datos

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3.10+ | Lenguaje principal |
| Flask | Framework web |
| SQLAlchemy | ORM para base de datos |
| PostgreSQL | Base de datos relacional |
| Flask-JWT-Extended | Autenticación con tokens |
| Flasgger / Swagger | Documentación interactiva |
| Flask-CORS | Permitir peticiones desde otros dominios |
| python-dotenv | Variables de entorno |

---

## 📁 Estructura del proyecto

```
mi_api/
├── app/
│   ├── __init__.py          # Inicializa Flask y registra extensiones
│   ├── config.py            # Configuración (lee el archivo .env)
│   ├── models/
│   │   ├── estudiante.py    # Tabla estudiantes
│   │   ├── materia.py       # Tabla materias
│   │   ├── calificacion.py  # Tabla calificaciones (relación muchos a muchos)
│   │   └── usuario.py       # Tabla usuarios
│   └── routes/
│       ├── __init__.py      # Rutas básicas (/, /health)
│       ├── estudiantes.py   # CRUD de estudiantes
│       ├── calificaciones.py# Calificaciones, materias y kardex
│       └── auth.py          # Registro, login y JWT
├── .env                     # Variables de entorno (NO subir a GitHub)
├── .gitignore
├── requirements.txt
└── run.py                   # Punto de entrada
```

---

## ⚙️ Instalación y configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/mi_api.git
cd mi_api
```

### 2. Crea el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura PostgreSQL

Abre pgAdmin o la terminal de PostgreSQL y ejecuta:

```sql
CREATE DATABASE mi_api_db;
CREATE USER flask_user WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE mi_api_db TO flask_user;
GRANT ALL ON SCHEMA public TO flask_user;
ALTER DATABASE mi_api_db OWNER TO flask_user;
```

### 5. Configura las variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=postgresql://flask_user:password123@localhost:5432/mi_api_db
JWT_SECRET_KEY=tu-jwt-clave-secreta-aqui
```

### 6. Ejecuta el servidor

```bash
python run.py
```

Deberías ver:
```
✅ Tablas creadas correctamente
🚀 Servidor iniciado en http://localhost:5000
📖 Documentación Swagger en http://localhost:5000/docs/
```

---

## 🗺️ Endpoints disponibles

### Rutas generales
| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/` | Bienvenida |
| GET | `/health` | Estado de la API |

### Estudiantes
| Método | URL | Descripción |
|--------|-----|-------------|
| POST | `/api/estudiantes/` | Crear nuevo estudiante |
| GET | `/api/estudiantes/` | Listar todos (con paginación y filtros) |
| GET | `/api/estudiantes/{id}` | Obtener un estudiante por ID |
| PUT | `/api/estudiantes/{id}` | Actualizar datos |
| DELETE | `/api/estudiantes/{id}` | Desactivar (borrado lógico) |

### Materias y Calificaciones
| Método | URL | Descripción |
|--------|-----|-------------|
| POST | `/api/materias/` | Crear materia |
| GET | `/api/materias/` | Listar materias |
| POST | `/api/calificaciones/` | Registrar calificación |
| GET | `/api/estudiantes/{id}/kardex` | Kardex con estadísticas |

### Autenticación
| Método | URL | Descripción |
|--------|-----|-------------|
| POST | `/api/auth/registro` | Registrar usuario |
| POST | `/api/auth/login` | Login → obtener token JWT |
| GET | `/api/auth/perfil` | Ver perfil (requiere token) |

---

## 🧪 Ejemplos de uso

### Crear un estudiante

```http
POST http://localhost:5000/api/estudiantes/
Content-Type: application/json

{
  "matricula": "ITIC2024001",
  "nombre": "Ana",
  "apellido": "García López",
  "email": "ana.garcia@uni.edu.mx",
  "carrera": "ITIC",
  "semestre": 5
}
```

**Respuesta:**
```json
{
  "mensaje": "Estudiante creado exitosamente",
  "estudiante": {
    "id": 1,
    "matricula": "ITIC2024001",
    "nombre_completo": "Ana García López",
    "carrera": "ITIC",
    "semestre": 5
  }
}
```

### Obtener kardex

```http
GET http://localhost:5000/api/estudiantes/1/kardex
```

**Respuesta:**
```json
{
  "estudiante": { "nombre": "Ana", "carrera": "ITIC" },
  "estadisticas": {
    "promedio_general": 87.5,
    "total_materias": 4,
    "materias_aprobadas": 4,
    "materias_reprobadas": 0,
    "estatus": "Regular"
  },
  "calificaciones": [...]
}
```

### Login

```http
POST http://localhost:5000/api/auth/login
Content-Type: application/json

{
  "username": "profe_juan",
  "password": "MiPassword123"
}
```

**Respuesta:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "tipo": "Bearer",
  "expira_en": "24 horas"
}
```

---

## 📖 Documentación interactiva

Una vez corriendo el servidor, accede a la documentación Swagger en:

```
http://localhost:5000/docs/
```

Desde ahí puedes probar todos los endpoints directamente en el navegador sin necesidad de Postman.

---

## 🎓 Conceptos aprendidos

- Patrón **Application Factory** en Flask
- **ORM con SQLAlchemy** — clases Python como tablas de base de datos
- Relaciones **Uno-a-Muchos** y **Muchos-a-Muchos** entre tablas
- Implementación de **CRUD completo** con métodos HTTP (GET, POST, PUT, DELETE)
- **Paginación** de resultados
- **Borrado lógico** (soft delete) como buena práctica
- **Autenticación JWT** — hasheo de contraseñas y tokens firmados
- **Variables de entorno** para datos sensibles
- **Documentación Swagger** con Flasgger

---

## 👩‍💻 Desarrollado por

**Edith** — Ingeniería en Tecnologías de la Información e Innovación Digital  
Ciclo Escolar 2025-2026 • Quinto Cuatrimestre-Hecho con pasiòn- Propiedad de Brenda Edith®
