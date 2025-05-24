from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)

# acabo de registrar en el apartado de admin el modelo task
# para poder ver el modelo se debe agregar en el admin.py de la aplicacion tasks
# y asi poder ver las tareas en el panel de administracion de django

# al crear la carpeta template la registro en el settings.py