from django.db import models

# Create your models here.
# crear una tabla de tareas
class Task(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
    
# ^el metodo __str__ se usa para que cuando se imprima el objeto, 
# se muestre el texto de la tarea
    