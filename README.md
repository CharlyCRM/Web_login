# Formulario de acceso con Flask y SQLite

Una práctica inicial para conectar un formulario HTML con una consulta SQLAlchemy. La aplicación comprueba si encuentra una fila coincidente con los dos campos introducidos.

## Qué contiene

`main.py` muestra el formulario y recibe POST en `/validar_usuario`. `models.py` define `usuarios` y `db.py` conecta con `database/logins.db`.

El resultado es un mensaje indicando si existe esa combinación. No crea una sesión autenticada ni un área privada.

## Antes de ejecutarlo

El ejercicio compara y almacena contraseñas como texto, sin hashing. No es un sistema seguro de autenticación: no debe utilizarse con contraseñas reales, datos personales ni acceso público. También arranca en debug.

Para revisar el flujo, usa un entorno aislado y una copia con datos ficticios:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requierements.txt
python main.py
```

El archivo se llama `requierements.txt`. Ejecuta desde la raíz y abre http://127.0.0.1:5000/. Con una base vacía se crean las tablas, pero no se registran usuarios automáticamente.

## Qué aprendí

Fue un primer contacto con formularios, modelos y consultas. Para convertirlo en autenticación real habría que rediseñar contraseñas, sesiones y protecciones del formulario. Esta revisión solo contextualiza el código original.
