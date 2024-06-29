# Django + Cloudinary ☁🐍

- Iniciamos creando nuestro entorno virtual

```bash
python -m venv venv#Recuerda puedes poner python -m venv mi_entorno_virtual
```

- Activar nuestro entorno virtual

```bash
.\venv\Scripts\activate#Powershell - CMDsource venv/Scripts/activate#GitBash
```

- Crear nuestro primer proyecto en django

```bash
pip install django

```

- Ahora iniciamos nuestro proyecto en django-admin

```bash
django-admin startproject core .

```

- Ahora creamos nuestra aplicacion con el nombre que deseemos

```bash
python manage.py startapp restaurante

```

> [!IMPORTANT] Cada vez que se cree una aplicacion en Django debemos de importar nuestra aplicacion dentro del settings.py
> 
- Antes de levantar el proyecto ejecutamos

```bash
python manage.py migrate

```

- Ahora ya podemos levantar nuestro proyecto

```bash
python manage.py runserver

```

## Django REST FRAMEWORK

- Instalamos Django REST FRAMEWORK

```bash
pip install djangorestframework

```

- Ahora dentro de settings añadimos la app rest_framework