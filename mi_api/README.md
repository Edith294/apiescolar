# 🐍 API REST con Flask + PostgreSQL
## Guía paso a paso para ejecutar el proyecto

---

## 📋 PASO 1 — Instalar PostgreSQL y crear la base de datos

1. Descarga e instala PostgreSQL desde https://www.postgresql.org/download/
2. Abre **pgAdmin** (se instala junto con PostgreSQL) o la terminal `psql`
3. Ejecuta estos comandos SQL (en pgAdmin: clic derecho en tu servidor → Query Tool):

```sql
CREATE DATABASE mi_api_db;
CREATE USER flask_user WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE mi_api_db TO flask_user;
```

✅ Listo. Ya tienes la base de datos creada.

---

## 📋 PASO 2 — Abrir la carpeta del proyecto en la terminal

Abre una terminal (CMD o PowerShell en Windows, Terminal en Mac/Linux) y navega hasta esta carpeta:

```bash
cd ruta/donde/guardaste/mi_api
```

Ejemplo en Windows:
```bash
cd C:\Users\TuNombre\Desktop\mi_api
```

---

## 📋 PASO 3 — Crear el entorno virtual

Un entorno virtual es una "burbuja" donde se instalan las librerías solo para este proyecto (no afecta tu Python global).

```bash
python -m venv venv
```

Ahora **actívalo**:

- En **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- En **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

Sabrás que está activo porque verás `(venv)` al inicio de tu terminal.

---

## 📋 PASO 4 — Instalar las dependencias

Con el entorno virtual activo, instala todas las librerías:

```bash
pip install -r requirements.txt
```

Espera a que termine. Esto instala Flask, SQLAlchemy, JWT, Swagger y todo lo necesario.

---

## 📋 PASO 5 — Revisar el archivo .env

El archivo `.env` ya viene configurado con valores por defecto. Si usaste una contraseña diferente al crear el usuario de PostgreSQL, edita la línea:

```
DATABASE_URL=postgresql://flask_user:password123@localhost:5432/mi_api_db
```

Cambia `password123` por la contraseña que pusiste tú.

---

## 📋 PASO 6 — Ejecutar el servidor

```bash
python run.py
```

Deberías ver en la terminal:
```
✅ Tablas creadas correctamente
🚀 Servidor iniciado en http://localhost:5000
📖 Documentación Swagger en http://localhost:5000/docs/
* Running on http://0.0.0.0:5000
```

---

## 📋 PASO 7 — Probar la API

Abre tu navegador o Postman y prueba estas URLs:

| URL | Método | ¿Qué hace? |
|-----|--------|-----------|
| http://localhost:5000/ | GET | Bienvenida |
| http://localhost:5000/health | GET | Verifica que funciona |
| http://localhost:5000/docs/ | GET | Documentación Swagger visual |

---

## 🧪 Ejemplos de prueba con Postman

### Crear un estudiante
- **Método:** POST
- **URL:** http://localhost:5000/api/estudiantes/
- **Body (JSON):**
```json
{
  "matricula": "ITIC2024001",
  "nombre": "Ana",
  "apellido": "García López",
  "email": "ana.garcia@uni.edu.mx",
  "carrera": "ITIC",
  "semestre": 5
}
```

### Ver todos los estudiantes
- **Método:** GET
- **URL:** http://localhost:5000/api/estudiantes/

### Crear una materia
- **Método:** POST
- **URL:** http://localhost:5000/api/materias/
```json
{
  "clave": "PROG101",
  "nombre": "Programación Web",
  "creditos": 5,
  "docente": "Ing. Ramírez"
}
```

### Registrar una calificación
- **Método:** POST
- **URL:** http://localhost:5000/api/calificaciones/
```json
{
  "estudiante_id": 1,
  "materia_id": 1,
  "calificacion": 87.5,
  "periodo": "2024-1"
}
```

### Ver kardex de un estudiante
- **Método:** GET
- **URL:** http://localhost:5000/api/estudiantes/1/kardex

### Registrar usuario
- **Método:** POST
- **URL:** http://localhost:5000/api/auth/registro
```json
{
  "username": "profe_juan",
  "email": "juan@uni.edu.mx",
  "password": "MiPassword123",
  "rol": "docente"
}
```

### Login (obtener token)
- **Método:** POST
- **URL:** http://localhost:5000/api/auth/login
```json
{
  "username": "profe_juan",
  "password": "MiPassword123"
}
```

### Ver perfil (ruta protegida con JWT)
- **Método:** GET
- **URL:** http://localhost:5000/api/auth/perfil
- **Header:** `Authorization: Bearer <pega aquí el token del login>`

---

## 📁 Estructura del proyecto

```
mi_api/
├── app/
│   ├── __init__.py        ← Crea la app Flask y conecta todo
│   ├── config.py          ← Configuración (lee el .env)
│   ├── models/
│   │   ├── estudiante.py  ← Tabla estudiantes en la BD
│   │   ├── materia.py     ← Tabla materias
│   │   ├── calificacion.py ← Tabla calificaciones
│   │   └── usuario.py     ← Tabla usuarios
│   └── routes/
│       ├── __init__.py    ← Rutas básicas (/, /health)
│       ├── estudiantes.py ← CRUD de estudiantes
│       ├── calificaciones.py ← Calificaciones y kardex
│       └── auth.py        ← Login y JWT
├── .env                   ← Variables secretas (NO subir a GitHub)
├── .gitignore
├── requirements.txt       ← Lista de librerías necesarias
├── run.py                 ← Punto de entrada: python run.py
└── README.md              ← Esta guía
```

---

## ❓ Solución de problemas frecuentes

**Error: `psycopg2 no encontrado`**
```bash
pip install psycopg2-binary
```

**Error: `could not connect to server`**
- Verifica que PostgreSQL esté corriendo (Services en Windows, o `pg_ctl status` en Mac)
- Verifica el usuario y contraseña en el archivo `.env`

**Error: `Address already in use`**
- El puerto 5000 ya está ocupado. Cambia el puerto en `run.py`:
  ```python
  app.run(host='0.0.0.0', port=5001, debug=True)
  ```
