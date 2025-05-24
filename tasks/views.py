
from django.views.generic import ListView
# ^importar la vista generica ListView para poder crear la vista de la lista de tareas
from .models import Task
# ^importar el modelo Task para poder usarlo en la vista


# Create your views here.
class TaskListView(ListView):
    model = Task
# ^especificar el modelo que se va a usar, relaciono modelo y template
    template_name = 'tasks-list.html'
# ^asociar el modelo con el template, y este con la vista 
    

    
