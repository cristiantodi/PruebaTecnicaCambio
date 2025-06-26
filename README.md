# 📰 Prueba Técnica - Desarrollador Backend Python/Django

**Empresa:** Cambio Colombia  
**Candidato:** Cristian Tole  
**Tecnologías:** Django, Django REST Framework, DRF-YASG, SQLite  

---

## ✅ Descripción del Proyecto

Este proyecto representa un sistema de gestión editorial tipo CMS con funcionalidades para:

- Registro de redactores
- Creación y administración de artículos
- Gestión de suscripciones
- Exposición de datos mediante una API RESTful
- Exportación de artículos a CSV
- Validación lógica de negocio
- Documentación automática con Swagger



## ⚙️ Instalación y ejecución

** 1. Clona el repositorio o descomprime el .zip**
```bash
git clone https://github.com/cristiantodi/PruebaTecnicaCambio.git
cd cms_project
```
** 2. Crea y activa un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

** 3. Instala dependencias**
```bash
pip install -r requirements.txt
```

** 4. Aplica migraciones**
```bash
python manage.py migrate
```

** 5. Crea superusuario (opcional para admin)**
```bash
python manage.py createsuperuser
```

** 6. Ejecuta el servidor
```bash
python manage.py runserver

Abre tu navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000). 
```

** 7. Estructura del proyecto
```bash
prueba
├───appPrueba
│   ├───api
│   │   └───__pycache__
│   ├───management
│   │   └───commands
│   │       └───__pycache__
│   ├───migrations
│   │   └───__pycache__
│   └───__pycache__
├───prueba
│   └───__pycache__
└───user
    ├───migrations
    │   └───__pycache__
    └───__pycache__
```




## 🧩 Comando personalizado

✅ GET /api/articulos/

✅ GET /api/articulos/?estado=publicado

✅ POST /api/articulos/

✅ GET /api/suscripciones/

✅ POST /api/suscripciones/ con validación:

👉 No permite suscripciones si ya existe una activa para el usuario.



## 🧪 Comando personalizado

✅  Swagger: http://localhost:8000/swagger/

✅ ReDoc: http://localhost:8000/redoc/


## 🧰  Herramientas utilizadas

✅ Python 3.12

✅ Django 5.2

✅ Django REST Framework 3.16

✅ drf-yasg

✅ SQLite

✅ Admin nativo de Django


## 📄 Preguntas escritas

1. ¿Qué buenas prácticas aplica al versionar código con Git?
```bash

Commits pequeños y con mensajes significativos.

Uso de ramas por funcionalidad (feature/api-articulos).

.gitignore bien configurado para excluir entorno, DB y migraciones temporales.

README claro y actualizado.
```

2. ¿Cómo abordaría el despliegue en producción?
```bash

Base de datos como PostgreSQL.

Servidor web Nginx.

HTTPS, variables de entorno, y control de acceso a admin.

Logs centralizados y monitoreo básico.
```

3. ¿Tiene experiencia previa trabajando en plataformas CMS o CRM?
4. 
```bash
Tengo experiencia en CRM con PressexLogistic en el cual realizamos un ERP en el cual se realiza un seguimiento un seguimiento de paqueteria, productos y clientes.
```

4. Indicar si se utilizó y en caso afirmativo explicar brevemente; la integración de
modelos built-in de Django, en especial el modelo auth.User con los modelos que
fueron creados para la aplicación.

```bash
No se utilizó directamente en esta prueba, sin embargo se realizo Override del user con el fin que si se extiende el proyecto se pueda manejar usuarios avanzados.
```
